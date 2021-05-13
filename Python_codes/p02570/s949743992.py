from collections import defaultdict
from collections import deque
from collections import Counter
import math

def readInt():
  return int(input())
def readInts():
  return list(map(int, input().split()))
def readChar():
  return input()
def readChars():
  return input().split()

d,t,s = readInts()

if d<=t*s:
  print("Yes")
else:
  print("No")