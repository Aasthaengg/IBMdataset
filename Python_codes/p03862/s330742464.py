N, x = map(int, input().split())

A = list(map(int, input().split()))

ans = 0

for i in range(1, N):
  dif = A[i-1] + A[i] - x
  if dif > 0:
    A[i] = max(0, A[i] - dif)
    ans += dif
    
print(ans)    