from math import factorial
n,blue = map(int, input().split())
red = n-blue
MOD = 10**9+7

def comb(n,r):
  return factorial(n)//factorial(r)//factorial(n-r)

for i in range(1, blue+1):
  if red + 1- i < 0:
    print(0)
    continue
  ans = comb(red+1, i)
  ans %= MOD
  ans *= comb(blue-1, i-1)
  ans %= MOD
  print(ans)