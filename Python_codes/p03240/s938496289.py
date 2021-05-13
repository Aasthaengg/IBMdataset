l=sorted([[*map(int,input().split())] for _ in range(int(input()))],key=lambda k:-k[2])
x,y,h=l[0]
for X in range(101):
  for Y in range(101):
    H=h+abs(x-X)+abs(y-Y)
    if all(h==max(H-abs(x-X)-abs(y-Y),0) for x,y,h in l): print(X,Y,H)