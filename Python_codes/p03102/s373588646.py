n,m,c = map(int, input().split())
B = list(map(int, input().split()))
count = 0
for i in range(n):
  A = list(map(int, input().split()))
  d = 0
  for j in range(m):
    d += A[j]*B[j]
  d += c
  if d > 0:
    count += 1
print(count)