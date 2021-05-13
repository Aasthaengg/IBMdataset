n,m = map(int, input().split())
a = [list(map(int,input().split())) for _ in range(n)]

a.sort()
b1=0
b2=0
c=0

for i in range(n):
  b1, b2 = b1+a[i][1], b1
  if b1 <= m:
    c += a[i][0] * a[i][1]
  else:
    c += a[i][0] * (m - b2)
    break

print(c)