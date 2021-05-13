import sys
input = sys.stdin.readline
n, m = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
M = 10**9 + 7
def get_diffsum(X, M):
  left_sum = sum(X)
  left_count = len(X)
  ans = 0
  for x in X:
    left_sum -= x
    left_count -= 1
    ans += left_sum - left_count * x
    ans %= M
  return ans

print(get_diffsum(X, M) * get_diffsum(Y, M) % M)
