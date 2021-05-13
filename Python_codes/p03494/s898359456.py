def solve():
  ans = 0
  N = int(input())
  A = list(map(int, input().split()))
  while True:
    for i in range(N):
      if A[i]%2==1:
        return ans
      A[i]//=2
    ans += 1
  return ans
print(solve())