n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]
s = 0
cnt = 0

for i in range(n-m+1):
    for j in range(n-m+1):
        for x in range(m):
            for y in range(m):
                if a[i+x][j+y] == b[x][y]:
                    s += 1
        if s == m ** 2:
            cnt += 1
        else:
            s = 0
if cnt > 0:
    print('Yes')
else:
    print('No')