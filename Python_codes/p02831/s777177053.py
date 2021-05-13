import fractions

def lcm(x,y):
  return(x*y)//(fractions.gcd(x,y))

A, B = list(map(int, input().split()))
print(lcm(A,B))