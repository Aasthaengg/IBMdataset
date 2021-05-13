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

a,b,c,d = readInts()

ans = b-a+1
ans-=b//c-(a-1)//c
ans-=b//d-(a-1)//d
ans+=b//(c*d//(math.gcd(c,d)))-(a-1)//(c*d//(math.gcd(c,d)))

print(ans)