a, b, k = map(int, raw_input().split())

for i in range(k/2):
  a /= 2
  b += a
  b /= 2
  a += b

if k % 2 == 1:
  a /= 2
  b += a

print('{} {}'.format(a, b))
