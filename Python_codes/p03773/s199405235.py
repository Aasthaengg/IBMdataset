a, b = map(int, input().split())
if 0 <= a <= 23 and 0 <= b <= 23:
  c = a + b
  if c >= 24:
    print(c - 24)
  else:
    print(c)