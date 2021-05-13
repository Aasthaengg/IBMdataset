def solve():
  N, K = map(int, input().split())
  H = [int(input()) for _ in range(N)]
  H.sort()
  ans = float('inf')
  for i in range(N):
    if i+K>N:
      break
    ans = min(H[i+K-1]-H[i],ans)
  return ans
print(solve())