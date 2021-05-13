import sys
n = int(input())
print(0)
sys.stdout.flush()
l = 0
r = n+1
x = input()
if x == "Vacant":
  exit()
prv = 0
while True:
  m = (l+r)//2
  print(m)
  sys.stdout.flush()
  y = input()
  if y == "Vacant":
    break
  if (x == y) ^ (prv%2 == m%2) == 0:
    if prv>m:
      r = m
    else:
      l = m
  else:
    if prv>m:
      l = m
    else:
      r = m
  prv = m
  x = y