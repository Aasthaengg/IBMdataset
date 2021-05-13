M, K = map(int, input().split())

N = 1 << M

if M == 0:
	if 0 < K:
		print(-1)
	else:
		print('0 0')
elif M == 1:
	if 0 < K:
		print(-1)
	else:
		print('0 0 1 1')
else:
	if N <= K:
		print(-1)
	else:
		RK = K
		A = [RK]
		B = [i for i in range(N) if i != RK]
		print(' '.join((
			' '.join(map(str, reversed(A))),
			' '.join(map(str, reversed(B))),
			' '.join(map(str, A)),
			' '.join(map(str, B)))))

