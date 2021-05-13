def solve():
  N = int(input())
  A = [int(input()) for _ in range(N)]
  ans = sum(A)
  if ans%10!=0:
    return ans
  A.sort()
  for i in range(N):
    if A[i]%10!=0:
      return ans-A[i]
  return 0
print(solve())