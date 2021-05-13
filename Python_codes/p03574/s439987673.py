a = []
dx = [1, 0, -1, 0, 1, -1, -1, 1]
dy = [0, 1, 0, -1, 1, 1, -1, -1]
h, w = map(int, input().split())
ans = [["#"] * w for _ in range(h)]

for _ in range(h):
    a.append(input())

for k in range(h):
    for j in range(w):
        if a[k][j] == ".":
            count = 0
            for i in range(8):
                nx = j + dx[i]
                ny = k + dy[i]

                if nx < 0 or ny < 0 or nx >= w or ny >= h:
                    continue
                if a[ny][nx] == "#":
                    count += 1
            ans[k][j] = count

for s in ans:
    print(*s, sep="")