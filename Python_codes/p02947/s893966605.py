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

def comb(n,r):
  return math.factorial(n)//math.factorial(r)//math.factorial(max(1,n-r))

def con(t):
  ans = ""
  for i in t:
    ans+=i[0]+str(i[1])
  return ans

n = readInt()
d = defaultdict(int)
for i in [input() for i in range(n)]:
  t = defaultdict(int)
  for j in i:
    t[j]+=1
  d[con(sorted(t.items()))]+=1
ans = 0
for i in d:
  ans+=comb(d[i],2)

print(ans)