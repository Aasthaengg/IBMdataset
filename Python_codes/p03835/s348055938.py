import sys

(K, S) = (int(x) for x in input().split())
comb = 0

for x in range(0, K + 1):
  for y in range(0, K + 1):
    z = S - x - y
    if z <= K and z >= 0:
#      print("%d %d %d" % (x, y, z))
      comb+=1

print(comb)