N = int(input())
A = [int(input()) for _ in range(N)]

cond = 0
for i in range(N):
	if A[i] % 2 == 1:
		cond = 1
		break

if cond:
	print('first')
else:
	print('second')