def solve():
  N, K = map(int, input().split())
  ans = (N//K)**3
  if K%2==0:
    ans += ((N+K//2)//K)**3
  return ans
print(solve())