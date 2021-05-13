n,m=map(int,input().split())
lb=0
ub=n
for i in range(m):
  l,r=map(int,input().split())
  lb=max(lb,l)
  ub=min(ub,r)
  
if ub>=lb:
  print(ub-lb+1)
else:
  print(0)