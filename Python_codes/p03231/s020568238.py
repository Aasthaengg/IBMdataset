from math import gcd
def solve():
  N, M = map(int, input().split())
  S = input()
  T = input()
  g = gcd(N,M)
  ans = N*M//g
  for i in range(g):
    if S[N//g*i]!=T[M//g*i]:
      return -1
  return ans
print(solve())