n , m = map(int,input().split())
kagi = []
for i in range(m):
    a , b = map(int,input().split())
    c = list(map(lambda x:int(x)-1,input().split()))
    k = 0
    for j in c:
        k += 2**j
    kagi.append((a,k))
dp = [[float("inf") for i in range(2**n)] for j in range(m+1)]
dp[0][0] = 0
for i in range(m):
    for j in range(2**n):
        dp[i+1][j] = min(dp[i][j],dp[i+1][j])
        dp[i+1][j | kagi[i][1]] = min(dp[i+1][j | kagi[i][1]],dp[i][j] + kagi[i][0])

if dp[-1][-1] != float("inf"):
    print(dp[-1][-1])
else:
    print(-1)