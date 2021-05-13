import sys
import math

for line in sys.stdin:
  a = line.split()
  if len(a) == 3:
    if (int(a[0])*int(a[0]) + int(a[1])*int(a[1])) == int(a[2])*int(a[2]) or (int(a[0])*int(a[0]) + int(a[2])*int(a[2])) == int(a[1])*int(a[1]) or (int(a[2])*int(a[2]) + int(a[1])*int(a[1])) == int(a[0])*int(a[0]):
    
        print("YES")
    else:
        print("NO")