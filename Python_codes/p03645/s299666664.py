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

import bisect
def isin(arr,x):
	#print(bisect.bisect_left(arr,x))
	return arr[min(bisect.bisect_left(arr,x),len(arr)-1)]==x

n,m = readInts()
ab = [readInts() for i in range(m)]
go1 = []
for i in range(m):
	if ab[i][0]==1:
		go1.append(ab[i][1])
go1.sort()
for i in range(m):
	if isin(go1,ab[i][0]) and ab[i][1]==n:
		print("POSSIBLE")
		exit()

print("IMPOSSIBLE")