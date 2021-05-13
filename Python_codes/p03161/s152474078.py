N,K=map(int, input().split())
A = list(map(int, input().split()))
 
INF = 10**9
dp = [INF]*N
 
for i in range(len(A)):
    if i == 0:
        dp[0] = 0
    elif i == 1:
        dp[1] = abs(A[1]-A[0])
    else:
        jmp = min(i,K)
        for j in range(1,jmp+1):
            dp[i] = min(dp[i], dp[i-j]+abs(A[i]-A[i-j]))
            
print(dp[N-1])