def solve():
  ans = 0
  cnt = 0
  N, K = map(int, input().split())
  A = [list(map(int, input().split())) for _ in range(N)]
  A.sort()
  for a,b in A:
    cnt += b
    if cnt>=K:
      ans = a
      break
  return ans
print(solve())