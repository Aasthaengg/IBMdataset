def solve():
  N, C, K = map(int, input().split())
  ans = 1
  cnt = 0
  T = [int(input()) for _ in range(N)]
  T.sort()
  for i in range(N):
    if i==0:
      now = T[i]
    cnt += 1
    if now+K<T[i] or cnt>C:
      ans += 1
      cnt = 1
      if i<N-1:
        now = T[i]
  return ans
print(solve())