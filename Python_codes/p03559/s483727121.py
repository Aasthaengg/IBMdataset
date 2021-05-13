N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A = sorted(A)
B = sorted(B)
C = sorted(C)

# for this we will use binary search.
import bisect as bis

BSC = [0]*N
ASB = [0]*N

for i in range (0, N):
	BSC[i] = N-bis.bisect_right(C, B[i])

for i in range (0, N):
	ASB[i] = bis.bisect_right(B, A[i])
    
for i in range (1, N):
	BSC[N-1-i] += BSC[N-i]

count = 0
for i in range (0, N):
	if ASB[i] ==N:
		continue
	else:
		count+=BSC[ASB[i]]

print(count)