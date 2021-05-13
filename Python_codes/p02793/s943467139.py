from fractions import gcd
def lcm(x,y):
  return (x*y) // gcd(x,y)
n = int(input())
a = list(map(int,input().split()))
mod = 10**9+7
l = a[0]
for i in range(1,n):
  l = lcm(l,a[i])
ans = 0
for i in range(n):
  ans += l//a[i]
print(ans%mod)