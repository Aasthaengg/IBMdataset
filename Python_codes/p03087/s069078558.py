N,Q=map(int,input().split())
S=input()
res=0
dp=[0]*N
a=0
for i in range(1,N):
  if S[i]=='C':
    if S[i-1]=='A':
      res+=1
  dp[i]=res
for _ in range(Q):
  l,r=map(int,input().split())
  if l==1:
    print(dp[r-1])
  else:
    print(dp[r-1]-dp[l-1])