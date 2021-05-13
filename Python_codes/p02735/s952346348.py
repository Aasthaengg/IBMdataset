H,W=map(int,input().split())
lst=[[] for f in range(H)]
ans=[[0 for e in range(W)] for f in range(H)]
for i in range(H):
 lst[i]=[(d) for d in input()]
for i in range(1,H):
 if lst[i][0]!=lst[i-1][0]:
  ans[i][0]=ans[i-1][0]+1
 else:
  ans[i][0]=ans[i-1][0]
for j in range(1,W):
 if lst[0][j]!=lst[0][j-1]:
  ans[0][j]=ans[0][j-1]+1
 else:
  ans[0][j]=ans[0][j-1]
for i in range(1,H):
 for j in range(1,W):
  if lst[i][j]==lst[i][j-1]:
   a=0
  else:
   a=1
  if lst[i][j]==lst[i-1][j]:
   b=0
  else:
   b=1
  ans[i][j]=min(ans[i][j-1]+a,ans[i-1][j]+b)
if lst[0][0]=="."and lst[H-1][W-1]==".":
 print((ans[H-1][W-1])//2)
elif lst[0][0]=="#"and lst[H-1][W-1]=="#":
 print((ans[H-1][W-1]+2)//2)
else:
 print((ans[H-1][W-1]+1)//2)