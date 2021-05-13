import numpy as np

sts = input()

st = sts.split(' ')
d = int(st[0])
t = int(st[1])
s = int(st[2])

# print(d)
# print(t)
# print(s)

if ((d/s) <= t):
  print('Yes')
else:
  print('No')

