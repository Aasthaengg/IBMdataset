"""
覚えておきたい
"""

n,*a=map(int,open(0).read().split())
ans=1
tmp=0
for i in range(1,n):
  if (a[i]-a[i-1])*tmp<0:
    ans+=1
    tmp=0
  elif not a[i]-a[i-1]==0:
    tmp=a[i]-a[i-1]
print(ans)