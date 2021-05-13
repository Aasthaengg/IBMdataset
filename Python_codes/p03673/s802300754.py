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
a = readInts()

if len(a)%2==0:
	for i in range(len(a)-1,0,-2):
		print(a[i], end=" ")
	for i in range(0,len(a),2):
		print(a[i], end=" ")
else:
	for i in range(len(a)-1,-1,-2):
		print(a[i], end=" ")
	for i in range(1,len(a),2):
		print(a[i], end=" ")