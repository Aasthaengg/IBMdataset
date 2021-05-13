h, w = map(int, input().split(" "))
s = []
for i in range(h):
    s.append(str(input()))
d = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
ss = ["" for i in range(h)]
for i in range(w):
    for j in range(h):
        if s[j][i] == "#":
            ss[j] += "#"
            continue
        cnt = 0
        for dx, dy in d:
            if 0 <= i + dx < w and 0 <= j + dy < h:
                if s[j + dy][i + dx] == "#":
                    cnt += 1
        ss[j] = ss[j] + str(cnt)

for i in ss:
    print(i)
