W, H, N=map(int, input().split())
hen=[0,W,0,H]
for _ in range(N):
  x, y, a=map(int, input().split())
  if a==1:
    hen[a-1]=max(hen[a-1], x)
  elif a==2:
    hen[a-1]=min(hen[a-1], x)
  elif a==3:
    hen[a-1]=max(hen[a-1], y)
  elif a==4:
    hen[a-1]=min(hen[a-1], y)
yoko=hen[1]-hen[0]
tate=hen[3]-hen[2]
if yoko<0 or tate<0:
  ans=0
else:
  ans=yoko*tate
print(ans)