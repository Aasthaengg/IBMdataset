from fractions import gcd
n,k=map(int,input().split())
a=list(map(int,input().split()))
g=0
for i in a:
  g=gcd(g,i)
print("POSSIBLE" if k%g==0 and max(a)>=k else "IMPOSSIBLE")