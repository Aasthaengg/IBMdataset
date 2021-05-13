n = int(input())
scale = 2 ** 30
while scale >= n:
  scale //= 2
#print('#',scale)
print(0)
z0 = input()
now = 0
while True:
  tmp = now + scale
  print(tmp%n)
  z1 = input()
  if z1 == 'Vacant':
    exit()
  if z1 == z0:
    now = tmp
  scale //= 2