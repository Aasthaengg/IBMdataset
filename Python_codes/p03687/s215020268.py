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
ans = float("inf")
s = input()
for i in s:
	t = s.split(i)
	l = -1
	for j in t:
		l = max(l,len(j))
	ans = min(ans,l)
print(ans)