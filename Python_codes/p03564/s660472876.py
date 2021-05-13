n = int(input())
k = int(input())

x = 1
for _ in range(n):
  if x > k:
    x += k
  else:
    x *= 2
print(x)