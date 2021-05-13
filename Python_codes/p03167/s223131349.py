h,w = map(int,input().split())
l = [['#']*(w+2)]
for i in range(h):
    l.append(['#']+list(input())+['#'])
l.append(['#']*(w+2))

mod = 10**9+7
dp = [[0]*(w+2) for _ in range(h+2)]

for i in range(1,h+1):
    for j in range(1,w+1):
        if i==1 and j==1:
            dp[1][1] = 1
            continue
        if l[i][j] == '.':
            dp[i][j] = (dp[i-1][j]+dp[i][j-1])%mod
print(dp[h][w])