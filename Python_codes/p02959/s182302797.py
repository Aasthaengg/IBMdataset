N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
for i in range(N):
  if A[i] >= B[i]:
    ans += B[i]
  else:
    ans += B[i]
    A[i+1] -= (B[i] - A[i])
    if A[i+1] < 0:
      ans -= abs(A[i+1])
      A[i+1] = 0
print(ans)