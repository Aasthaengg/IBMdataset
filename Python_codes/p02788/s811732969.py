def nibun_right(a, x, lo=0, hi=None):
 if lo < 0:
  raise ValueError('lo must be non-negative')
 if hi is None:
  hi = len(a)
 while lo < hi:
  mid = (lo+hi)//2
  if x < a[mid][0]: hi = mid
  else: lo = mid+1
 return lo
def nibun_right(a, x):
 lo, hi = 0, len(a)
 while lo < hi:
  mid = (lo+hi)//2
  if x < a[mid][0]: hi = mid
  else: lo = mid+1
 return lo
N,D,A=map(int,input().split())
lst=[0]*N
for i in range(N):
 lst[i]=list(map(int,input().split()))
lst.sort()
DMG=[0]*(N+1)
ans=0
for i in range(N):
 renji=nibun_right(lst,lst[i][0]+2*D)
 Z=max(int((lst[i][1]-1)/A)+1-DMG[i],0)
 DMG[i]+=Z
 DMG[renji]-=Z
 ans+=Z
 DMG[i+1]+=DMG[i]
print(ans)
