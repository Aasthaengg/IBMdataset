# A - Poisonous Cookies
A, B, C = map(int, input().split())

if A + B < C:
	print(A + B * 2 + 1)
else:
	print(B + C)