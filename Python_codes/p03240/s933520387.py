f=lambda:map(int,input().split())
n=int(input())
lh,lz=[],[]
for _ in range(n):
  x,y,h=f()
  if h: lh+=[(x,y,h)]
  else: lz+=[(x,y)]
for X in range(101):
  for Y in range(101):
    x,y,h=lh[0]
    H=h+abs(x-X)+abs(y-Y)
    for x,y,h in lh:
      if H!=h+abs(x-X)+abs(y-Y): break
    else:
      if all(H-abs(x-X)-abs(y-Y)<1 for x,y in lz):
        print(X,Y,H)