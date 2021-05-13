n, m, c = map(int, input().split())
b = list(map(int, input().split()))
ans=0
y = []

for i in range(n):
  a = map(int, input().split())
  A = list(a)
  for j in range(m):
    x = A[j] * b[j]
    y.append(int(x))
  if sum(y) + c <= 0:
    ans += 0
  else:
    ans += 1
  y.clear()
print(ans)