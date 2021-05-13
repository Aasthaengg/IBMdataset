N, Q = map(int, input().split())
S = input()

count = [0] * N

for i in range(N-1):
	
	if S[i] == 'A' and S[i+1] == 'C':
		count[i] = 1

accum = count.copy()
for i in range(1, N):
	accum[i] += accum[i-1]

for i in range(Q):
	l, r = map(int, input().split())
	l -= 1; r -= 1;
	if l == 0:
		res = accum[r]
	else:
		res = accum[r] - accum[l-1]
	if count[r] == 1:
		res -= 1
	print(res)