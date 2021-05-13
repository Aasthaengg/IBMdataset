import sys
  
def gcd(m,n):
    return m if n==0 else gcd(n, m%n)

for m,n in [map(int,x.split()) for x in list(sys.stdin)]:
    g = gcd(m,n)
    print(g,(m//g)*n)