from collections import defaultdict
from collections import deque
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

n = readInt()
h = readInts()
ans = 0
while h.count(0)!=n:
  boo = 0
  for i in range(len(h)):
    if h[i]!=0:
      if boo==0:
        boo=1
        ans+=1
      h[i]-=1
    else:
      boo=0

print(ans)