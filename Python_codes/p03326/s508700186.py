n,m=map(int,input().split())
x,y,z=[],[],[]
for i in range(n):
  xi,yi,zi=map(int,input().split())
  x.append(xi)
  y.append(yi)
  z.append(zi)

ans=0
for i in range(2**3):
  op=['-','-','-']
  for j in range(3):
    if (i>>j)&1:
      op[j]='+'

  tx=x[::]
  ty=y[::]
  tz=z[::]

  if op[0]=='-':
    tx=list(map(lambda a : -1*a, tx))
  if op[1]=='-':
    ty=list(map(lambda a : -1*a, ty))
  if op[2]=='-':
    tz=list(map(lambda a : -1*a, tz))

  xyz_l=[tx[i]+ty[i]+tz[i] for i in range(n)]
  xyz_l.sort(reverse=True)

  ans=max(ans,sum(xyz_l[:m]))

print(ans)