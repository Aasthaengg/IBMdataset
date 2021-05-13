n,m,x=map(int,input().split())
a=list(map(int,input().split()))
a.sort(key=int)
down=0
up=0
for i in range(m):
  if n>=a[i]>x:
    up+=1
  elif a[i]<x:
    down+=1
print(min(up,down))