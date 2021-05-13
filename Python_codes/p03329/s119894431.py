N = int(input())

A = [1]

for i in range (1, 7):
	A.append(6**i)

for i in range (1, 6):
	A.append(9**i)
    
A = sorted(A)
import math
DP = [math.inf]*1000001
DP[0] = 0

for i in range (0, 1000001):
	for j in range (0, 12):
		if i+A[j] < 1000001:
			if  DP[i]+1 < DP[i+A[j]]:
				DP[i+A[j]] = DP[i]+1
print(DP[N])