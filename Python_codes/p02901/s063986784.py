n, m = map(int,input().split())
a = [0]
b = [0]
c = [0]*(m+1)
for i in range(1, m+1):
    tab = list(map(int, input().split()))
    a.append(tab.pop(0))
    b.append(tab)
    tc1 = list(map(int, input().split()))
    tc2 = 0
    for j in tc1:
        tc2 |= 1<<(j-1)
    c[i] = tc2
INF = 10**9
dp = [[0] + [INF] * (2**n-1) for i in range(m+1)]
for i in range(1, m+1):
    for j in range(2**n):
        dp[i][j] = min(dp[i][j], dp[i-1][j])
        nj = j | c[i]
        dp[i][nj] = min(dp[i][nj], dp[i-1][nj], dp[i-1][j] + a[i])

print(-1) if dp[m][2**n-1] == INF else print(dp[m][2**n-1])