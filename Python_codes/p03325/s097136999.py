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
a = readInts()
ans = 0
for i in range(n):
	while 1:
		if a[i]%2==0:
			a[i]=a[i]//2
			ans+=1
		else:
			break

print(ans)