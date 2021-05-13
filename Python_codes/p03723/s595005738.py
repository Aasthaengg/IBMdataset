a, b, c = map(int, input().split())
t = 0

if a == b == c:
  if a % 2 == 1:
    print(t)
  else:
    print(-1)

else:
  while (a % 2 + b % 2 + c % 2) == 0:
    a, b, c = (b + c) / 2, (a + c) / 2, (a + b) / 2
    t += 1

  print(t)