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

def comb(n,r):
  return math.factorial(n)//math.factorial(r)//math.factorial(n-r)

def cula(a):
  ans = 0
  for i in range(a+1):
    ans+=comb(a,i)
  return ans

def culb(b):
  ans = 0
  for i in range(p,b+1,2):
    ans+=comb(b,i)
  return ans

n,p = readInts()
a = [0,0]
for i in readInts():
  if i%2==0:
    a[0]+=1
  else:
    a[1]+=1

print(cula(a[0])*culb(a[1]))