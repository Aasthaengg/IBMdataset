def count1(c):
  cnt = 0
  while c != 0:
    if c % 2 == 1:
      cnt += 1
    c //= 2
  return cnt
n = int(input())
x = input()
y = int(x, 2)
z = list(x).count('1')
l = []
a = y % (z + 1)
if z > 1:
  l2 = []
  b = y % (z - 1)
for i in range(n):
  l.append(pow(2, n - i - 1, z + 1))
  if z > 1:
    l2.append(pow(2, n - i - 1, z - 1))
for i in range(n):
  if x[i] == '0':
    c = a + l[i]
    c %= z + 1
  elif z == 1 and x[i] == '1':
    print(0)
    continue
  else:
    c = b - l2[i]
    c %= z - 1
  cnt = 1
  while c != 0:
    d = count1(c)
    c %= d
    cnt += 1
  print(cnt)