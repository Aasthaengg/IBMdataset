n, a, b = map(int, input().split(' '))

max = 0
min = 0

if a > b:
  max = b
  min = b - (n - a)
else:
  max = a
  min = a - (n - b)

if min < 0:
  min = 0

# print(n, a, b)
print('{} {}'.format(max, min))
