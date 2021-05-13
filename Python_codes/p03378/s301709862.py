n,m,x=map(int, input().split())
a=list(map(int, input().split()))
down=0
up=0
for i in a:
  if i<x:
    down+=1
  elif i>x:
    up+=1
print(min(down,up))