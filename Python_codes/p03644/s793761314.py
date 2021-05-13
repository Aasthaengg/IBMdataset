import sys
n = int(input())
for i in range(n):
  m = n-i
  for j in range(0,7):
    if 2**j == m:
      print(m)
      sys.exit()