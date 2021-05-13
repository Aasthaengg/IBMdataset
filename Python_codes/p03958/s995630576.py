k,t=map(int,input().split())
a=[int(x) for x in input().split()]
a.sort()
now1=0
now2=0
al=sum(a)
ans=float('inf')
for i in range(t):
  now1+=a[i]
  now2=al-now1
  ans=min(ans,abs(now1-now2)-1)

if ans<=0:
  print(0)
else:
  print(ans)
