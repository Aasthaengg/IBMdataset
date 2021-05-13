n,m,x=map(int,input().split())
A=list(map(int,input().split()))
costright,costleft=0,0
for a in A:
  if a>x:
    costright+=1
  else:
    costleft+=1

print(min(costright,costleft))