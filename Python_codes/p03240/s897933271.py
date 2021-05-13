from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n=int(input())
l=[]
for i in range(n):
  x,y,h=nii()
  l.append([x,y,h])
  if h!=0:
    ini_x=x
    ini_y=y
    ini_h=h

for tx in range(101):
  for ty in range(101):
    n_h=abs(tx-ini_x)+abs(ty-ini_y)+ini_h
    for x,y,h in l:
      t_h=max(n_h-(abs(tx-x)+abs(ty-y)),0)
      if h!=t_h:
        break
    else:
      print(tx,ty,n_h)
      exit()