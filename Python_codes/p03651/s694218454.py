
from fractions import gcd
from functools import reduce

def solve():
  n, k = list(map(int, input().split()))
  a = list(map(int, input().split()))

  l = reduce(gcd, a)
  max_a = reduce(max, a)
  if k % l == 0 and max_a >= k:
    print("POSSIBLE")
  else:
    print("IMPOSSIBLE")

  return
 
if __name__ == "__main__":
  solve()