N = int(input())
K = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(N):
  if A[i] <= K/2:
    ans += 2*A[i]
  else:
    ans += 2*(K-A[i])
print(ans)