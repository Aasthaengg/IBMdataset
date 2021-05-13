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
s = input()
t = input()

if s==t and len(s)>=n:
  print(len(s))
  exit()
if n>=len(s)+len(t):
  print(n)
  exit()

de = 0
for i in range(min(len(s),len(t))):
  if s[i*-1-1:]==t[:i+1]:
    de = i+1

print(len(s)+len(t)-de)