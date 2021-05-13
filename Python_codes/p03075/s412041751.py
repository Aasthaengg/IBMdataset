import itertools
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())

arr1 = [a, b, c, d, e]
arr2 = [b, c, d, e]
f = 0
for x, y in itertools.product(arr1, arr2):
  if abs(x - y) > k:
    f += 1
if f == 0:
  print('Yay!')
else:
  print(':(')
