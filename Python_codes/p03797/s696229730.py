n, m = map(int, input().split())

if n*2 <= m:
  t = n*2 + m
  print(t//4)
else:
  print(m//2)