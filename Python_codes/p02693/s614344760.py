from collections import defaultdict

def readInt():
	return int(input())
def readInts():
	return list(map(int, input().split()))
def readChar():
	return input()
def readChars():
	return input().split()

k = int(input())
a,b  = readInts()

for i in range(a,b+1):
	if i%k==0:
		print("OK")
		exit()

print("NG")