a, b, c, d = map(int, input().split())
i = 0
while a > 0 and c > 0:
  if i % 2 == 0:
    c -= b
  else:
    a -= d
  i += 1
print("Yes" if a > 0 else "No")