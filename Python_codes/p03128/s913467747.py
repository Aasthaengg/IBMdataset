n,m=map(int,input().split())
A=[2,5,5,4,5,6,3,7,6]
B=list(map(int,input().split()))
B=sorted(B,reverse=True)
C=[]
for i in range(m):
  C.append(A[B[i]-1])
C=set(C)
C=sorted(list(C))
dp=[-10**10]*(n+10)
dp[0]=0
for i in range(1,n+1):
  for j in range(len(C)):
    if dp[i]<dp[i-C[j]]+1:
      dp[i]=dp[i-C[j]]+1
S=[]
for i in range(dp[n]):
  for j in range(len(B)):
    if dp[n-A[B[j]-1]]==dp[n]-1:
      n=n-A[B[j]-1]
      S.append(B[j])
      break
for i in range(len(S)):
  print(S[i],end="")
print()