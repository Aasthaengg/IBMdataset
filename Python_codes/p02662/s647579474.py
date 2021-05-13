N,S=map(int,input().split())
A=[0]+list(map(int,input().split()))
mod=998244353

#print(A)

DP=[[0 for i in range(S+1)]for j in range(N+1)]

DP[0][0]=1

for i in range(1,N+1):
    for j in range(S+1):
        if j-A[i]>=0:
            DP[i][j]=(DP[i-1][j]*2+DP[i-1][j-A[i]])%mod
        else:
            DP[i][j]=(DP[i-1][j]*2)%mod
print(DP[-1][-1])