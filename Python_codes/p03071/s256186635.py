import sys
rm = lambda: map(int, sys.stdin.buffer.readline().split())
a, b = rm()
if a == b:
  print(a*2)
else:
  print(max(a, b)*2-1)