n = int(input())
g = [[1] * n for _ in range(n)]
for i in range(n-1 if n % 2 else n):
    j = n-i-2 if n % 2 else n-i-1
    g[i][j], g[j][i] = 0, 0
print((n*(n-1)//2)-n//2)
for i in range(n):
    for j in range(i+1, n):
        if g[i][j]: print(i+1, j+1)
