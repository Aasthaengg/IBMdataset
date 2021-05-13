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

d = defaultdict(int)
n = readInt()
for c in [input() for i in range(n)]:
	d[c[0]]+=1
tar = [d["M"],d["A"],d["R"],d["C"],d["H"]]
ans = 0
for a in itertools.combinations(tar,3):
	ans+=a[0]*a[1]*a[2]

print(ans)