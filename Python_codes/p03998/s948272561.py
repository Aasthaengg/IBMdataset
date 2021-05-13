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

a = list(input())
b = list(input())
c = list(input())

def solve(tar):
  if len(eval(tar))==0:
    print(tar.upper())
    exit()
  if tar=="a":
    x = a[0]
    del a[0]
    solve(x)
  elif tar=="b":
    x = b[0]
    del b[0]
    solve(x)
  else:
    x = c[0]
    del c[0]
    solve(x)
solve("a")