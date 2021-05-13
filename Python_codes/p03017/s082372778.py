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

n,a,b,c,d = readInts()
a-=1
b-=1
c-=1
d-=1
s = readChar()
if (a-b)*(c-d)<0:
  if "..." in s[b-1:d+2] and "##" not in s[a:c]:
    print("Yes")
  else:
    print("No")
else:
  if "##" not in s[a:d+1]:
    print("Yes")
  else:
    print("No")