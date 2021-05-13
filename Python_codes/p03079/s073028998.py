import sys
input = sys.stdin.readline

# A - Regular Triangle
A, B, C = map(int, input().split())

if A == B and A == C and B == C:
	print('Yes')
else:
	print('No')