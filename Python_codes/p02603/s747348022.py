N = int(input())
A = list(map(int, input().split()))

amount = 1000
MX = A[0]
MN = A[0]

for i in range(1, N):
	a = A[i]
	if a < MX:
		if MN < MX:
			s = amount // MN
			t = amount % MN
			amount = MX * s + t
		MN = a
		MX = a
	else:
		if a > MX:
			MX = a
		if a < MN:
			MN = a

	if i == N - 1 and MN < MX:
		s = amount // MN
		t = amount % MN
		amount = MX * s + t

print(amount)