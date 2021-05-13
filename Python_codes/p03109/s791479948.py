import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
if s[5:5+2] > '04':
  print('TBD')
else:
  print('Heisei')