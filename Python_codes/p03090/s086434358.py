n = int(input())

g = [[1] * (n + 1) for _ in range(n + 1)]

if n % 2:
    for i in range(1, n + 1):
        j = n - i
        g[i][j] = 0
        g[j][i] = 0

else:
    for i in range(1, n + 1):
        j = n + 1 - i
        g[i][j] = 0
        g[j][i] = 0

ans = []
for i, row in enumerate(g[1:], 1):
    for j, bl in enumerate(row[i+1:], i+1):
        if bl:
            ans.append((i, j))

print(len(ans))
for i, j in ans:
    print(i, j)
