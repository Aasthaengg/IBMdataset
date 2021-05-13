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

a,b,c = readInts()

if ((c-a-b)**2-4*a*b)>0 and c-a-b>0:
	print("Yes")
else:
	print("No")