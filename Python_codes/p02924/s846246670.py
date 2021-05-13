from collections import defaultdict
import bisect

def readInt():
	return int(input())
def readInts():
	return list(map(int, input().split()))
def readChar():
	return input()
def readChars():
	return input().split()


n = readInt()
print(n*(n-1)//2)