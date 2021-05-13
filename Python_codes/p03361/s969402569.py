flag = False
a = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

h, w = map(int, input().split())

for i in range(h):
    a.append(input())

for k in range(h):
    for j in range(w):
        if a[k][j] == "#":
            for i in range(4):
                nx = j + dx[i]
                ny = k + dy[i]

                if nx < 0 or ny < 0 or nx >= w or ny >= h:
                    continue
                if a[ny][nx] == "#":
                    break
            else:
                flag = True
                print("No")
        if flag:
            break
    if flag:
        break
else:
    print("Yes")