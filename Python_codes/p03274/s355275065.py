import bisect
n,k = map(int, input().split())
x = list(map(int, input().split()))
z = bisect.bisect_left(x,0)

ans=10**12
s=z-k
if s < 0:
  s=0
g=z+1
if g+k >= n:
  g=n-k+1
for i in range(s,g):

  xl=x[i]
  xr=x[i+k-1]
  ans=min(ans,abs(xr)+abs(xr-xl),abs(xl)+abs(xr-xl))
print(ans)