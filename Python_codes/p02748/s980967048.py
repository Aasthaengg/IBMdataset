A, B, M = input().split(' ')
A = int(A)
B = int(B)
M = int(M)
a = input().split(' ')
a = [int(a[i]) for i in range(A)]
b = input().split(' ')
b = [int(b[i]) for i in range(B)]
cost = min(a) + min(b)
for i in range(M):
  x, y, c = input().split(' ')
  x = int(x)-1
  y = int(y)-1
  c = int(c)
  if a[x] + b[y] - c < cost:
    cost = a[x] + b[y] - c
print(cost)