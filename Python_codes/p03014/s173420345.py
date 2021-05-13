h, w = map(int, input().split())
s = []
for _ in range(h):
    s.append(input())
lis_row = [[0 for j in range(w)] for i in range(h)]
lis_column = [[0 for j in range(w)] for i in range(h)]
for i in range(h):
    tmp = 0
    lis = []
    for j in range(w):
        if s[i][j] == "#":
            lis.append(0)
            tmp = 0
        else:
            tmp += 1
            lis.append(tmp)
    now = 0
    for j in range(w-1, -1, -1):
        if lis[j] != 0:
            now = max(lis[j], now)
            lis_row[i][j] = now
        else:
            now = 0

for j in range(w):
    tmp = 0
    lis = []
    for i in range(h):
        if s[i][j] == "#":
            lis.append(0)
            tmp = 0
        else:
            tmp += 1
            lis.append(tmp)
    now = 0
    for i in range(h-1, -1, -1):
        if lis[i] != 0:
            now = max(lis[i], now)
            lis_column[i][j] = now
        else:
            now = 0
ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            ans = max(ans, lis_row[i][j] + lis_column[i][j] -1)
print(ans)