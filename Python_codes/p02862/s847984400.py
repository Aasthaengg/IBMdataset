import sys
 
X, Y = map(int, input().split())
def combination(n, r, mod=10**9+7):
    n1, r = n+1, min(r, n-r)
    numer = denom = 1
    for i in range(1, r+1):
        numer = numer * (n1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod-2, mod) % mod

if 2*Y < X or 2*X < Y or (X+Y)%3 != 0:
  print(0)
  sys.exit()
  
n1 = (2*Y-X)//3
n2 = (2*X-Y)//3

print(combination(n1+n2, min(n1, n2), 10**9+7))