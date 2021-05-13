N, K = map(int, input().split())
A = list(map(int, input().split()))
#dp[k] 0 => lose of turn player 1 => win of turn player
dp = [-1 for i in range(K+1)]
for i in range(min(A)):
    dp[i] = 0
for k in range(1,K+1):
    if dp[k] > 0:
        continue
    if all(dp[k-a] == 1 for a in A if k - a >= 0): #どんな減らし方をしても手番が負け
        dp[k] = 0
    else:
        dp[k] = 1
print(['Second', 'First'][dp[-1]])