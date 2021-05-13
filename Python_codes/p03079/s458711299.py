A, B, C = map(int, input().split())
if A + B > C and B + C > A and C + A > B and A == B == C:
	print("Yes")
else:
	print("No")
