from math import gcd
N = int(input())
A = list(map(int, input().split()))
k = 0
for i in A:
  k = gcd(i,k)
print(k)