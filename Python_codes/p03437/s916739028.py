def gcd(p,q):
      if p%q==0:
            return q
      else:
            return gcd(q,p%q)

x,y=map(int,input().split())
g=gcd(x,y)
if g==y:
      print(-1)
else:
      print(x)
