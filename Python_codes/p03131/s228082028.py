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

k,a,b = readInts()

if a+1<=k and a+2<b:
	k-=a+1
	ans=k//2*(b-a)+k%2+b
else:
	ans = k+1

print(ans)