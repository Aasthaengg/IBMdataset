N,M=map(int,input().split())
xyz=[list(map(int,input().split())) for i in range(N)]

ans=0
for i in range(2**3):
  F=[1]*3
  for j in range(3):
    if (i>>j)&1:
      F[j]=-1
  xyz.sort(reverse=True, key=lambda x:F[0]*x[0]+F[1]*x[1]+F[2]*x[2])
  x=0
  y=0
  z=0
  val=0
  for k in range(M):
    x+=xyz[k][0]
    y+=xyz[k][1]
    z+=xyz[k][2]
  val=abs(x)+abs(y)+abs(z)
  ans=max(ans,val)
print(ans)