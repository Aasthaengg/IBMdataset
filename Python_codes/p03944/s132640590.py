from collections import defaultdict
from collections import deque
from collections import Counter
import itertools
import math

def readInt():
  return int(input())
def readInts():
  return list(map(int, input().split()))
def readChar():
  return input()
def readChars():
  return input().split()

w,h,n = readInts()
xya = [readInts() for i in range(n)]

xmin = 0
xmax = w
ymin = 0
ymax = h

for x,y,a in xya:
  if a==1:
    xmin = max(x,xmin)
  elif a==2:
    xmax = min(x,xmax)
  elif a==3:
    ymin = max(y,ymin)
  else:
    ymax = min(y,ymax)

print(max(0,xmax-xmin)*max(0,ymax-ymin))