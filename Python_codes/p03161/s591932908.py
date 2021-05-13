N,K=list(map(int,input().split()))
A=list(map(int,input().split()))
dp=[0]*(N)
dp[0]=0
dp[1]=abs(A[1]-A[0])

for i in range(2,N):
    mina=10**9
    for j in range(1,K+1):
        if(i-j>=0):
            mina=min(dp[i-j]+abs(A[i]-A[i-j]),mina)
    dp[i]=mina
# print(dp)
print(dp[N-1])