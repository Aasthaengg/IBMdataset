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

n,k = readInts()

x = 0

for i in range(1,n+1):
	t=min(1/(2**math.ceil(math.log2(k)-math.log2(i))),1)
	x+=t
	#print(t)

print(x/n)