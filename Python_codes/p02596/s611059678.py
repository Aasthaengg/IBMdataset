import sys

k = int(input())

a = 0

for i in range(1, k+1):
	a = (a*10+7)%k
	if a == 0:
		print(i)
		sys.exit()
print(-1)