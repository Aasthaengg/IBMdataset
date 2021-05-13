R = str(input())
G = str(input())


if R[0] == G[2] and R[2] == G[0] and R[1] == G[1]:
	print('YES')
else:
	print('NO')