def solve():
  N = int(input())
  A = list(map(int, input().split()))
  A.sort(reverse=True)
  ans = sum(A[1:2*N:2])
  return ans
print(solve())