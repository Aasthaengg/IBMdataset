from collections import defaultdict

def readInt():
	return int(input())
def readInts():
	return list(map(int, input().split()))
def readChar():
	return input()
def readChars():
	return input().split()

n,m = readInts()
ab = [readInts() for i in range(n)]
ab.sort()
i = 0
ans = 0
while m>0:
	if m>=ab[i][1]:
		m-=ab[i][1]
		ans+=ab[i][0]*ab[i][1]
		i+=1
	else:
		ans += m*ab[i][0]
		m = 0
print(ans)