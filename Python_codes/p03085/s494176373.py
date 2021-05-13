import sys
rr = lambda: sys.stdin.readline().rstrip()
a = rr()
if a in 'AT':
  print('AT'.replace(a, ''))
else:
  print('GC'.replace(a, ''))













