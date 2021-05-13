n = int(input())
a = list(map(int, input().split()))

cnt = 0
b = []
c = []
for i in range(n):
  if i == 0:
    b.append(a[i])
  elif i % 2 == 0:
    b.append(a[i])
  elif i % 2 == 1:
    c.append(a[i])

if n % 2:
  ans = b[::-1] + c
else:
  ans = c[::-1] + b
print(*ans)
