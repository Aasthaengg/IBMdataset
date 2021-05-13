def solve():
  ans = 0
  mod = 10**9+7
  N, K = map(int, input().split())
  A = list(map(int, input().split()))
  for i in range(N):
    for j in range(i+1,N):
      if A[i]>A[j]:
        ans += 1
  ans *= K
  A.sort()
  lis = [0]*N
  for i in range(1,N):
    if A[i]>A[i-1]:
      lis[i] = i
    else:
      lis[i] = lis[i-1]
  ans += sum(lis)*K*(K-1)//2
  ans %= mod
  return ans
print(solve())