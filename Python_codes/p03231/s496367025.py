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

n,m = readInts()
s = readChar()
t = readChar()

d = defaultdict(str)

l = n*m//math.gcd(n,m)
j = 0
for i in range(1,(n-1)*(l//n)+1+1,l//n):
  d[i]=s[j]
  j+=1
j = 0
for i in range(1,(m-1)*(l//m)+1+1,l//m):
  if not (d[i]=="" or d[i]==t[j]):
    #おつかれサンバ
    print(-1)
    exit()
  j+=1
print(l)