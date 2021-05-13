l=[]
for _ in range(int(input())):
  t=[*map(int,input().split())]
  l+=[t]
  if t[2]: x,y,h=t
for X in range(101):
  for Y in range(101):
    H=h+abs(x-X)+abs(y-Y)
    if all(h==max(H-abs(x-X)-abs(y-Y),0) for x,y,h in l): print(X,Y,H)