n, a, b = (int(_) for _ in input().split())
if a > b or (n == 1 and a != b): print(0)
else:
  m, M = (n-1) * a + b, a + (n-1) * b
  print(M - m + 1)
