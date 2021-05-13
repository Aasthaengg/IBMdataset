n, m = map(int, input().split())
ss = input().split()
ts = input().split()
d = [[1] * (m+1) for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        d[i+1][j+1] = (d[i][j+1] + d[i+1][j] - (ss[i] != ts[j])*d[i][j]) % (10**9+7)
print(d[n][m])
