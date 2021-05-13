from collections import Counter
def solve():
  N, K = map(int, input().split())
  A = list(map(int, input().split()))
  C = Counter(A)
  ans = sum(sorted(C.values())[:len(C)-K])
  return ans
print(solve())