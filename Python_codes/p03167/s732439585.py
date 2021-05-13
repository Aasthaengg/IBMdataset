import sys
input = sys.stdin.readline
H,W= map(int,input().split())
mod=10**9+7
chk=[[0] for f in range(H)]
ans=[[0 for e in range(W)] for f in range(H)]
ans[0][0]=1
for i in range(H):
 chk[i]=[d for d in input()]
for i in range(1,W):
 if chk[0][i]==".":
  ans[0][i]=ans[0][i-1]
for i in range(1,H):
 if chk[i][0]==".":
  ans[i][0]=ans[i-1][0]
for i in range(1,H):
 for j in range(1,W):
  if chk[i][j]==".":
   ans[i][j]=ans[i-1][j]+ans[i][j-1]
   ans[i][j]%=mod
print(ans[H-1][W-1])
