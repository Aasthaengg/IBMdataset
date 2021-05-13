N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
for i in range(N+1):
  if i >= 1:
    p = min(A[i], B[i-1])
    ans += p
    A[i] -= p
  if i < N:
    p = min(A[i], B[i])
    ans += p
    B[i] -= p
print(ans)