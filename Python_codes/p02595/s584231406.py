n,d = list(map(int, input().split()))
c=0
d *= d
for i in range(n):
  x,y = list(map(int, input().split()))
  x *= x
  y *= y
  y += x
  if y <= d:
    c += 1
print(c)