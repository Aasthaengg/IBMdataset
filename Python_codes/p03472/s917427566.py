n, h = map(int, input().split())
h2 = h
l = []
for i in range(n):
  l.append(list(map(int,input().split())))

l_b = sorted(l, key=lambda x: x[1])
l = sorted(l_b, reverse=True, key=lambda x: x[0])
c_a = 0
c_b = 0
b_sum = 0

for i in range(n-1, -1, -1):
  if l_b[i][1] >= l[0][0]:
    b_sum += l_b[i][1]
    h -= l_b[i][1]
    c_b += 1
    if h <= 0:
      print(c_b)
      exit()
import math
c_a = math.ceil((h2 - b_sum) / l[0][0])


print(c_a+c_b)
