
def gcd(a,b):
  if a<b: a,b=b,a
  c=a%b
  if c==0:
    print(b)
  else:
    return gcd(b,c)

a,b = map(int, input().split())
gcd(a,b)
