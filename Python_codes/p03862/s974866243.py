N, x = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
i = 0
while i < N-1:
  if A[i]+A[i+1] > x:
    d = A[i]+A[i+1]-x
    ans += d
    A[i+1] = 0 if A[i+1] < d else A[i+1]-d
  i += 1
print(ans)