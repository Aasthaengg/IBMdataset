import sys

(n, m, l) = sys.stdin.readline().rstrip('\r\n').split(' ')
n = int(n)
m = int(m)
l = int(l)

a = []
b = []
c = []
for ii in range(n):
  a.append([int(x) for x in input().rstrip('\r\n').split(' ')])

for ii in range(m):
  b.append([int(x) for x in input().rstrip('\r\n').split(' ')])

for ii in range(n):
  c.append([])
  for jj in range(l):
    c[ii].append(0)
    for kk in range(m):
      c[ii][jj] += a[ii][kk] * b[kk][jj]
    c[ii][jj] = str(c[ii][jj])
  print(' '.join(c[ii]))

