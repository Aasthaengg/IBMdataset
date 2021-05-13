def cin():  return list(map(int,input().split()))

N, K = cin()
A = cin()

dp = [[-1 for _ in range(2)] for _ in range(100)]
dp[0][0] = 0
MAX_DIGIT = 50

for i in range(1, MAX_DIGIT):
    mask = (1 << (MAX_DIGIT - i - 1))
    cnt = 0
    for j in range(N):  cnt += bool(A[j] & mask)
    cost0 = mask * cnt
    cost1 = mask * (N - cnt)
    if(dp[i - 1][1] != -1):  dp[i][1] = max(dp[i][1], dp[i - 1][1] + max(cost0, cost1))
    if(dp[i - 1][0] != -1):
        if(K & mask):  dp[i][1] = max(dp[i][1], dp[i - 1][0] + cost0)
        if(K & mask):  dp[i][0] = max(dp[i][0], dp[i - 1][0] + cost1)
        else:  dp[i][0] = max(dp[i][0], dp[i - 1][0] + cost0)
        
ans = max(dp[MAX_DIGIT - 1][0], dp[MAX_DIGIT - 1][1])
print(ans)