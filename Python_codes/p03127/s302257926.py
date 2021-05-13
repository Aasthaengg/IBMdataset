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
a = list(set(readInts()))

if len(a)==1:
  print(a[0])
  exit()

odd = []
even = []


from math import gcd


d = a[0]
for i in a:
  d = gcd(i,d)
print(d)