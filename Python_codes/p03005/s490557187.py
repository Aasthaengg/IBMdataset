N,K = map(int,input().split())

if K == 1:
	print(0)
	exit()

minNum = 1
maxNum = N - (K-1)

print(maxNum - minNum)