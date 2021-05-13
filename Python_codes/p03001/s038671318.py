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

w,h,x,y = readInts()

if x==w/2 and y==h/2:
	d = 1
else:
	d = 0

print(w*h/2,d)