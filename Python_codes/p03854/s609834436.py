S = str(input())

counter = 0

T = len(S)
K = T//5+1

for i in range (0, K+1):
	T = len(S)
	if S[-5::] == 'dream':
		S = S[0:T-5]
	elif S[-5::] == 'erase':
		S = S[0:T-5]
	elif S[-7::] == 'dreamer':
		S = S[0:T-7]
	elif S[-6::] == 'eraser':
		S = S[0:T-6]

if len(S) == 0:
	print('YES')
else:
	print('NO')