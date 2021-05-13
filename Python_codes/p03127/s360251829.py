from math import gcd
def multi_gcd(A):
  g = A[0]
  for a in A:
    g = gcd(g,a)
  return g

def solve():
  N = int(input())
  A = list(map(int, input().split()))
  ans = multi_gcd(A)
  return ans
print(solve())
