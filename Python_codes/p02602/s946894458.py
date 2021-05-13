import sys
input = sys.stdin.readline

# C - Marks
N, K = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
	if i >= K:
		
		if A[i] > A[i - K]:
			print('Yes')
		else:
			print('No')