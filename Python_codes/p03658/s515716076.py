from itertools import groupby, accumulate, product, permutations, combinations
def solve():
  N, K = map(int, input().split())
  L = list(map(int, input().split()))
  L.sort(reverse=True)
  ans = sum(L[:K])
  return ans
print(solve())