r = int(input())
if r >= 2800:
  print('AGC')
  exit()
if r >= 1200:
  print('ARC')
  exit()
if r < 1200:
  print('ABC')