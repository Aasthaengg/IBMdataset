import sys
n = input()
d = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
for i in range(n):
  b, f, r, v = map(int, raw_input().split())
  d[b-1][f-1][r-1] += v
for i in range(4):
  for j in range(3):
    for k in range(10):
      sys.stdout.write(' %d' % d[i][j][k])
    if k==9:
      sys.stdout.write('\n')
  if j==2 and i<=2:
    sys.stdout.write('####################\n')