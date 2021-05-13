from fractions import gcd

n = int(input())
a = list(map(int, input().split()))
mod = 10**9 + 7

lcm = 1
for i in range(n):
  lcm = lcm * a[i] // gcd(lcm, a[i])
lcm %= mod

sum_b = 0
for i in range(n):
  sum_b = (sum_b + lcm * pow(a[i], mod - 2, mod)) % mod
print(sum_b)