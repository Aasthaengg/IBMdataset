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
sum_a = 3**n
pro = 1
for i in a:
	if i%2==0:
		pro*=2
print(sum_a-pro)