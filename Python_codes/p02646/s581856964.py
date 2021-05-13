a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())
if (a >= b):
  a, b = b, a
if (b + (w * t)) <= (a + (v * t)):
  print('YES')
else:
  print('NO')
