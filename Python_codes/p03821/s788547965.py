def solve():
  ans = 0
  N = int(input())
  A = [0]*N
  B = [0]*N
  for i in range(N):
    A[i],B[i] = map(int, input().split())
  for i in range(N-1,-1,-1):
    A[i] += ans
    if A[i]%B[i]>0:
      ans += B[i]-A[i]%B[i]
  return ans
print(solve())