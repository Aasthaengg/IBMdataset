from heapq import nlargest

n = int(input())
a = [int(input()) for i in range(n)]
b = nlargest(2, a)
ma = max(a)
for j in a:
  if j == ma:
    print(b[1])
  else:
    print(ma)