N=int(input())
A=[int(input()) for _ in range(N)]
mod=10**9+7
B=[A[0]-1]
for i in range(1,N):
  if A[i]!=A[i-1]:
    B.append(A[i]-1)
n=len(B)
used=[-1]*(max(A)+1)
used[B[0]]=0
dp=[0]*n
dp[0]=1
for i in range(1,n):
  if used[B[i]]==-1:
    dp[i]=dp[i-1]
  else:
    a=used[B[i]]
    dp[i]=(dp[i-1]+dp[a])%mod
  used[B[i]]=i
print(dp[-1])