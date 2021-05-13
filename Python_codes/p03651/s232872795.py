def gcd(a,b):
  while b:a,b=b,a%b
  return a
n,k=map(int,input().split())
a=list(map(int,input().split()))
g=a[0]
for i in a[1:]:g=gcd(g,i)
ans="IMPOSSIBLE"
for i in a:
  if k>i:continue
  if abs(k-i)%g==0:ans="POSSIBLE"
print(ans)