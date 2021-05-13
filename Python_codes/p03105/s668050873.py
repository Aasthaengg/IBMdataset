A, B, C = map(int, input().split())

if (A*C <= B):
	print(C)
else:
	ans = int(B/A)
	print(ans)