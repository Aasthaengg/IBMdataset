from heapq import nlargest
import sys
n = int(input())
a = [int(input()) for i in range(n)]
l1, l2 = nlargest(2, a)

if l1 == l2:
  for i in range(n):
    print(l1)
  sys.exit()

for i in a:
  if i == l1:
    print(l2)
  else:
    print(l1)
