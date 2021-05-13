n,t = map(int,input().split())
orders = []
for i in range(n):
    a,b = map(int,input().split())
    orders.append([a,b])

orders.sort(key=lambda x:(x[0],-x[1]))
# print(orders)

dp = [[-1e10 for i in range(t+1)] for j in range(n+1)]
dp[0][0] = 0

for i,od in enumerate(orders):
    for j in range(t+1):
        dp[i+1][j] = dp[i][j]
    for j in range(t):
        nt = j+od[0]
        if nt > t-1:
            nt = t
        if dp[i+1][nt] < dp[i][j]+od[1]:
            dp[i+1][nt] = dp[i][j]+od[1]

# for l in dp:
#     print(l[:11])
# print(dp[-1])
print(max(dp[-1]))