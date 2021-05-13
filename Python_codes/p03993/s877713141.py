from collections import defaultdict

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
for i in range(len(a)):
	if a[a[i]-1]==i+1:
		ans+=1
print(ans//2)