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
d = defaultdict(int)
for i in [input() for j in range(n)]:
  d["".join(sorted(i))]+=1

from math import factorial as f

ans = 0
for i in d:
  if d[i]>1:
    ans+=f(d[i])//f(2)//f(d[i]-2)

print(ans)