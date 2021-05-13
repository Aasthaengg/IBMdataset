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

d = defaultdict(int)

for i in input():
	d[i]+=1
#print(d)
if abs(d["a"]-d["b"])<2 and abs(d["b"]-d["c"])<2 and abs(d["a"]-d["c"])<2:
	print("YES")
else:
	print("NO")