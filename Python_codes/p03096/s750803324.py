from bisect import bisect_left
p = 10**9+7
N = int(input())
C = [int(input()) for _ in range(N)]
A = [0 for _ in range(N)]
B = {i:[0,-1] for i in range(1,2*10**5+1)}
for i in range(N):
    c = C[i]
    if B[c][-1]==i-1:
        A[i] = 0
    else:
        A[i] = 1
    B[c].append(i)
dp = [0 for _ in range(N+1)]
dp[1] = 1
for i in range(1,N):
    if A[i]==1:
        ind = bisect_left(B[C[i]],i)
        j = B[C[i]][ind-1]
        dp[i+1] = (dp[i]+dp[j+1])%p
    else:
        dp[i+1] = dp[i]
print(dp[N])