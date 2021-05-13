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

x = readInt()
ans = math.ceil((-1+(x*8)**0.5)/2)
print(ans)