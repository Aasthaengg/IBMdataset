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

n = readInt()
d = defaultdict(int)
for i in readChars():
	d[i]+=1
m =readInt()
t = defaultdict(int)
for i in readChars():
	t[i]+=1

for key in t:
	if d[key]-t[key]<0:
		print("NO")
		exit()
print("YES")