a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

dist = abs(a - b)
kasoku = v - w

if dist > kasoku * t:
  print('NO')
else:
  print('YES')