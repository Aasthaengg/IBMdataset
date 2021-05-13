import bisect
from math import ceil
n,d,a=map(int,input().split())
XH=[list(map(int,input().split())) for i in range(n)]
X=[XH[i][0] for i in range(n)]
XH.sort(key=lambda y:y[0])
X.sort()
damage=[0]*(n+1)
ans=0
for i,(x,h) in enumerate(XH):
  damage[i]+=damage[i-1]
  h-=damage[i]
  if h<=0:
    continue
  cnt=ceil(h/a)
  ans+=cnt
  damage[i]+=a*cnt
  br=bisect.bisect_right(X,x+d*2)
  damage[br]-=a*cnt
print(ans)