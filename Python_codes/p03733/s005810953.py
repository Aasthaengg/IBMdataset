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

n,t = readInts()
ts = readInts()
end = ts[0]+t
ans = t

for i in ts:
	ans+=min(t-(end-i),t)
	end = i+t

print(ans)