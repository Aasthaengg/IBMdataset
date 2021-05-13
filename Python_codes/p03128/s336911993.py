N,M=list(map(int,input().split()))
A=sorted(list(map(int,input().split())),reverse=True)
C=[-1,2,5,5,4,5,6,3,7,6]
DP=[[0 if j==0 else -1 for i in range(M)] for j in range(N+1)]
for i in range(N+1):
  for j in range(M):
    if(j>0):
      DP[i][j]=max(DP[i][j],DP[i][j-1]);
    if(i-C[A[j]]>=0 and DP[i-C[A[j]]][j]!=-1):
      DP[i][j]=max(DP[i][j],DP[i-C[A[j]]][j]*10+A[j]);
    if(j>0 and i-C[A[j]]>=0 and DP[i-C[A[j]]][j-1]!=-1):
      DP[i][j]=max(DP[i][j],DP[i-C[A[j]]][j-1]*10+A[j]);
print(DP[N][M-1])  