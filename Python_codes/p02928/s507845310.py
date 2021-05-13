N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
  tmp = 0
  for j in range(i+1, N):
    if A[i] > A[j]:
      tmp += 1
  tmp *= K*(K+1)//2
  ans += tmp
  tmp = 0
  for j in range(i):
    if A[i] > A[j]:
      tmp += 1
  tmp *= K*(K-1)//2
  ans += tmp
  ans = ans % (10**9+7)
print(ans)