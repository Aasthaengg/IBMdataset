W,H,N=map(int,input().split())
vec=[[False]*W for i in range(H)]
for i in range(N):
  x,y,a=map(int,input().split())
  if a==1:
    for i in range(x):
      for j in range(H):
        vec[j][i]=True
  elif a==2:
    for i in range(x,W):
      for j in range(H):
        vec[j][i]=True
  elif a==3:
    for i in range(W):
      for j in range(y):
        vec[j][i]=True
  else:
    for i in range(W):
      for j in range(y,H):
        vec[j][i]=True
ans=0
for i in range(W):
  for j in range(H):
    if vec[j][i]==False:
      ans+=1
print(ans)
