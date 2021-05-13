import sys
N = sys.stdin.readline().strip().split()
l = list(sys.stdin.readline().strip())
r = l.count('R')
b = l.count('B')

if r > b:
  print('Yes')
else:
  print('No')