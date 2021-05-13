def solve():
  N, x = map(int, input().split())
  A = list(map(int, input().split()))
  A.sort()
  ans = 0
  for i in range(N):
    if i==N-1:
      if A[i]==x:
        ans += 1
      continue
    if x>=A[i]:
      ans += 1
      x -= A[i]
  return ans
print(solve())