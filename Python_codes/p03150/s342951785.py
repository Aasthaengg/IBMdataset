from collections import defaultdict
from collections import deque
import itertools
import copy

def readInt():
	return int(input())
def readInts():
	return list(map(int, input().split()))
def readChar():
	return input()
def readChars():
	return input().split()

s = input()

l = len(s)-7


w = "keyence"
j=0
for i in range(len(s)):
	if s[i]==w[j]:
		j+=1
	else:
		if s[i+l:]==w[j:]:
			print("YES")
		else:
			print("NO")
		exit()

print("YES")