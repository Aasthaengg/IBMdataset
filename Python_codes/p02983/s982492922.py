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

l,r = readInts()

ans = float("inf")
for i in range(l,min(r+1,l+2020)):
  for j in range(i+1, min(r+1,l+2020)):
    ans = min(ans,(i*j)%2019)

print(ans)