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

n = readInt()
s = [readInt() for i in range(n)]
s.sort()
ans = sum(s)
boo = 0
if ans%10==0:
	for i in s:
		if i%10!=0:
			ans-=i
			boo = 1
			break
	if boo==0:
		ans = 0

print(ans)