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

n = readInt()
ab = [readInts() for i in range(n)]
ab.sort(key=lambda x:x[1])
now = 0
for i in ab:
  now+=i[0]
  if now<=i[1]:
    pass
  else:
    print("No")
    exit()

print("Yes")