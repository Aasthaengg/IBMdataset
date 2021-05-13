def solve():
  ans = 0
  N, M = map(int, input().split())
  A = [list(map(int, input().split())) for _ in range(N)]
  A.sort()
  for i in range(N):
    if M>=A[i][1]:
      ans += A[i][0]*A[i][1]
      M -= A[i][1]
    else:
      ans += A[i][0]*M
      break
  return ans
print(solve())