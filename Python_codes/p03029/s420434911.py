A, P = map(int, input().split())

x = (A * 3) + P

if x >= 2:
  y = x / 2
else:
  y = 0

print(int(y))