n,k=map(int,input().split())
a=list(map(int,input().split()))
def gcd(a,b):
  while b:a,b=b,a%b
  return a
g=a[0]
for i in a:g=gcd(g,i)
if max(a)>=k and k%g==0:print("POSSIBLE")
else:print("IMPOSSIBLE")