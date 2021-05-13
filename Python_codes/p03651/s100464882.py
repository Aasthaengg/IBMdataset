n,k=map(int,input().split())
a=list(map(int,input().split()))
if k>max(a):
  print("IMPOSSIBLE")
  exit(0)

from fractions import gcd
gcd_v=a[0]
for i in range(1,n):
  gcd_v=gcd(a[i],gcd_v)
for aa in a:
  if (aa-k)%gcd_v==0:
    print("POSSIBLE")
    exit(0)
print("IMPOSSIBLE")


