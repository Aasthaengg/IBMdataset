#c[i][j]=数字iから数字jにかえるのに必要な最小の魔力
H,W=list(map(int,input().split()))
c=[[i for i in range(10)] for j in range(10)]
for i in range(10):
  s=list(map(int,input().split()))
  for j in range(10):
    c[i][j]=s[j]

#ワーシャルフロイド法
for k in range(10):
  for i in range(10):
    for j in range(10):
      c[i][j]=min(c[i][k]+c[k][j],c[i][j])

ans=0
for i in range(H):
  a=list(map(int,input().split()))
  for j in range(W):
    if a[j]!=-1:
      ans=ans+c[a[j]][1]
print(ans)

