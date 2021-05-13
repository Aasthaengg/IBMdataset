import sys

ri = lambda: int(sys.stdin.readline())

if ri() == 1:
  print('Hello World')
  exit()
else:
  print(ri()+ri())