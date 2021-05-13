n = int(input())
a = map(int, input().split())
b = map(int, input().split())

d = 0
c = 0
for x, y in zip(a, b):
  if x < y:
    d += (y - x) // 2
  else:
    c += x - y

print('Yes' if d >= c else 'No')
