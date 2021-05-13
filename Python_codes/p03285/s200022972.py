import math
n = int(input())
# 4, 7
f = []
s = []
tmp = 0
ans = 0
a = math.floor(n/4)
b = math.floor(n/7)
cnt = 0
for i in range(a):
  f.append(4)
if (n % 4) == 0:
  cnt = 1
for i in range(0, len(f)):
  ans = (n-4*i) % 7
  if ans == 0:
    cnt = 1
    break
  ans = 0
if cnt == 1:
  print('Yes')
else:
  print('No')