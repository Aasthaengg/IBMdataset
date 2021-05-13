from collections import defaultdict
from collections import deque
from collections import Counter
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
b = readInts()

d = deque()

def renzoku(arr):
	i = -1
	boo = 1
	for i in range(1,len(arr)+1):
		#print(arr[len(arr)-i],len(arr)-i+1)
		if arr[len(arr)-i] == len(arr)-i+1:
			boo = 0
			break
	if boo:
		print(-1)
		exit()
	#print("return :",len(arr)-i)
	return len(arr)-i


for i in range(len(b)):
	r = renzoku(b)
	#print(b)
	#print(b[r])
	d.append(r)
	del b[r]

for i in reversed(d):
	print(i+1)