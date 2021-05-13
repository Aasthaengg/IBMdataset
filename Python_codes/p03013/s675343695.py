N, M = map(int, input().split())

A = []

for i in range (0, M):
	A.append(int(input()))


if N == 1:
	print(1)
	exit()
elif N ==2:
	if len(A) ==1:
		print(1)
	else:
		print(2)
	exit()

DP = [0]*N

if A.count(1)==0:
	DP[0] = 1

if A.count(2)==0:
	if A.count(1)==0:
		DP[1] = 2
	else:
		DP[1] = 1

for i in range (0, M):
	DP[A[i]-1] = -1

for i in range (0, 2):
	if DP[i] == -1:
		DP[i] = 0

for i in range (2, N):
	if DP[i] ==-1:
		DP[i] = 0
	else:
		DP[i] = DP[i-1] + DP[i-2]

print(DP[-1]%(1000000007))