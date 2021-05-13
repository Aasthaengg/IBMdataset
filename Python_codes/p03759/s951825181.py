a, b, c = map(int, input().split())
if 1 <= a <= 100 and 1 <= b <= 100 and 1 <= c <= 100:
  if b - a == c - b:
    print('YES')
  elif a - b == b - c:
    print('YES')
  else:
    print('NO')