a, b = map(int, input().split())
ans = ''

if a <= b:
  for _ in range(b):
    ans += str(a)
  print(int(ans))
else:
  for _ in range(a):
    ans += str(b)
  print(int(ans)) 