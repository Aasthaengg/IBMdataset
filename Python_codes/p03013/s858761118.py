#https://atcoder.jp/contests/abc129/tasks/abc129_c
N,M = map(int,input().split())
dp = [[] for i in range(N)]
for i in range(M):
    dp[int(input())-1] = 0

for i in range(N):
    if dp[i] != 0:
        if i == 0:
            dp[i] = 1
        elif i == 1:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1] + dp[i-2]
        
print(dp[-1] % 1000000007)     