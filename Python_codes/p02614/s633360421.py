from itertools import product

H,W,K=map(int,input().split())
masu=[input() for _ in range(H)]
ans=0
ROW=list(product([False,True],repeat=H))
COL=list(product([False,True],repeat=W))
for row in ROW:
  for col in COL:
    cnt=0
    for i in range(H):
      for j in range(W):
        if row[i]==False and col[j]==False and masu[i][j]=="#":
          cnt+=1
    if cnt==K:
      ans+=1
print(ans)
