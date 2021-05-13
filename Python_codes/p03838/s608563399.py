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

x,y = readInts()

if abs(x)==abs(y):
  if x==y:
    print(0)
  else:
    print(1)
elif x==0:
  if y>0:
    print(y)
  else:
    print(abs(y)+1)
elif y==0:
  if x>0:
    print(1+x)
  else:
    print(abs(x))
elif abs(x)<abs(y):
  if x>0 and y>0:
    print(y-x)
  elif x>0 and y<0:
    print(abs(y)-x+1)
  elif x<0 and y>0:
    print(x+y+1)
  else:
    print(abs(y)-abs(x)+2)
else:
  if x>0 and y>0:
    print(2+x-y)
  elif x>0 and y<0:
    print(1+x+y)
  elif x<0 and y>0:
    print(1+abs(x)-y)
  else:
    print(y-x)