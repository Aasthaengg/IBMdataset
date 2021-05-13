x = int(input())
import sys
for i in range(121):
  for j in range(-121,121):
    if i**5 - (j**5) == x:
      print(i,j)
      sys.exit()

