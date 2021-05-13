N,K = map(int,input().split())
A = list(map(int,input().split()))
dp = [0 for _ in range(K+1)]
for i in range(K+1):
    if i<A[0]:
        dp[i] = 0
    else:
        dp[i] = not dp[i-A[0]]
        for j in range(1,N):
            if i>=A[j]:
                dp[i] = dp[i] or not dp[i-A[j]]
if dp[K]==True:
    print("First")
else:
    print("Second")