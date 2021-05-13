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

def f(a,b):
  return math.ceil(a/b)*b-a

n = readInt()
ab = [readInts() for i in range(n)]
ans = 0
for a,b in ab[::-1]:
  ans += f(a+ans,b)

print(ans)