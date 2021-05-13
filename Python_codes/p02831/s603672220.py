def gcd(x,y):
 if y==0:return x
 else:return gcd(y, x % y)
def lcm(x,y):
  return x/gcd(x, y)*y;
print(int(lcm(*map(int,input().split()))))