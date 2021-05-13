n, k = map(int,input().split())
hl = list(map(int,input().split()))

dp = [[] for _ in range(n)]
dp[0] = 0

for i in range(1,n):
    tmp = float('inf')
    for j in range(1,k+1):
        if i-j < 0:
            continue
        tmp = min(dp[i-j] + abs(hl[i]-hl[i-j]),tmp)
    dp[i] = tmp
print(dp[-1])