import itertools
n,m=map(int,input().split())
xyz=[list(map(int,input().split())) for _ in range(n)]
ans=0
for a,b,c in itertools.product([-1,1],repeat=3):
  tmp=[]
  for x,y,z in xyz:
    tmp.append(a*x+b*y+c*z)
  tmp.sort(reverse=True)
  ans=max(ans,sum(tmp[:m]))
print(ans)