A, P = map(int,input().split())

if A == 0 and P < 2:
	print(0)
else:
	print((A * 3 + P ) // 2)