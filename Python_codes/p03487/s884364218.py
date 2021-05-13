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
c = Counter(readInts())

ans = 0
for i in c:
	if c[i]-i>0:
		ans+=c[i]-i
	elif c[i]-i<0:
		ans+=c[i]

print(ans)