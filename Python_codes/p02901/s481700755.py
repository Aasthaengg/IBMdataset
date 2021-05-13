n , m = map(int,input().split())
kagi = []
for i in range(m):
    a , b = map(int,input().split())
    c = list(map(int,input().split()))
    k = 0
    for j in c:
        k += 1 << (j-1)
    kagi.append((a,k))
INF = 10 ** 9
dp = [[INF for i in range(m+1)] for i in range(2**n)]
dp[0] = [0 for i in range(m+1)]
for i in range(2**n):
    for j in range(1,m+1):
        dp[i][j] = min(dp[i][j],dp[i][j-1])
        t = i | kagi[j-1][1]
        dp[t][j] = min(dp[t][j],dp[i][j]+kagi[j-1][0])
print(dp[2**n-1][m] if dp[2**n-1][m] != INF else -1)