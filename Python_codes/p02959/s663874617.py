N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

res = 0
for i in range(N):
  a = A[i]
  b = B[i]
  d = max(min(a, b), 0)
  res += d
  
  r = b - d
  if r > 0:
    d = min(A[i+1], r)
    A[i+1] -= d
    res += d
print(res)