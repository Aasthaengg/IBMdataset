n = int(input())
arr = list(map(int,input().split()))
xor = 0
for i in arr:
	xor ^= i
for i in arr:
	print(i^xor,end = ' ')