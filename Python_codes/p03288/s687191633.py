import sys
ri = lambda: int(sys.stdin.readline())

a = ri()
if a < 1200:
  print('ABC')
  exit()
print('ARC' if a < 2800 else 'AGC')