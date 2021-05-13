n,m=[int(x) for x in input().split()]
L=0
R=1000000
for i in range(m):
  l,r=[int(x) for x in input().split()]
  L=max(L,l)
  R=min(R,r)
ans=R-L+1
if ans<=0:
  print(0)
else:
  print(ans)