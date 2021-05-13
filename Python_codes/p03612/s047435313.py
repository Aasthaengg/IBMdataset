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
p = readInts()
ans = 0
for i in range(n-1):
	if i+1==p[i]:
		p[i],p[i+1]=p[i+1],p[i]
		ans+=1

if p[-1]==n:
	ans+=1

print(ans)