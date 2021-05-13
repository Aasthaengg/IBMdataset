a, b, n = map(int, input().split())
c = 0
d = a
i = 1
while d <= n:
  c = c + b
  i = i + 1
  d = a * i
print(c)