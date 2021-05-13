def solve():
  ans = 0
  N = int(input())
  A = list(map(int, input().split()))
  for i in range(N):
    A[i] -= i+1
  B = sorted(A)
  p = B[N//2]
  for i in range(N):
    A[i] = abs(A[i]-p)
  ans = sum(A)
  return ans
print(solve())