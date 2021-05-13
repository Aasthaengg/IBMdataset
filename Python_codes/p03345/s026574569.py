import sys
input = sys.stdin.readline

# A - Fairness
A, B, C, K = map(int, input().split())

if K % 2 == 0:
	print(A - B)
else:
	print(B - A)