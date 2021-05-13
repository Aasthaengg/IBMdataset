# D - Non-decreasing

import math

N = int(raw_input())
a = map(int, raw_input().split())
a_abs = [ math.fabs(i) for i in a ]
a_start = a_abs.index(max(a_abs))

if a[a_start] > 0:
  print N*2
  for message in range(2): print str(a_start+1) + " 1"
  for i in range(1, N):
    for message in range(2): print str(i) + " " + str(i+1)
elif a[a_start] < 0:
  print N*2
  for message in range(2): print str(a_start+1) + " " + str(N)
  for i in range(N-1, 0, -1):
    for message in range(2): print str(i+1) + " " + str(i)
else: print 0