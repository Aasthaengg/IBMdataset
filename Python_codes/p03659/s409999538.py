def solve():
  N = int(input())
  A = list(map(int, input().split()))
  a = sum(A)
  ans = float('inf')
  s = 0
  for i in range(N-1):
    s += A[i]
    ans = min(abs(a-2*s),ans)
  return ans
print(solve())