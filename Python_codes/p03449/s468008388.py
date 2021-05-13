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
a.extend(readInts())
ans = 0
for i in range(n):
	pos = 1
	t=a[0]
	for j in range(n):
		if i==j:
			pos+=n-1
		t+=a[pos]
		pos+=1
	ans = max(ans,t)
print(ans)