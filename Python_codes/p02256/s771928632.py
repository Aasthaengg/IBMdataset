def gcd(x,y):
  x,y=max(x,y),min(x,y)
  if y==0:
    return x
  else:
    return gcd(y, x%y)

a,b=map(int,input().split())
ans=gcd(a,b)
print(ans)
