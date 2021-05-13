from collections import defaultdict
def solve():
  d = defaultdict(lambda: 0)
  N = int(input())
  A = list(map(int, input().split()))
  mod = 10**9+7
  d[0] = 3
  ans = 1
  for i in range(N):
    if d[A[i]]==0:
      return 0
    ans *= d[A[i]]
    ans %= mod
    d[A[i]] -= 1
    d[A[i]+1] += 1
  return ans
print(solve())