n, a = map(int, input().split())
b = list(map(int, input().split()))
b.sort()
c = 0
for i in range(n):
  if a < b[i] or (i == n - 1 and b[i] != a):
    break
  a -= b[i]
  c += 1
print(c)