from math import gcd
n = int(input())
alst = list(map(int, input().split()))
ans = alst[0]
for a in alst:
  ans = gcd(ans, a)
print(ans)