def resolve():
	ins = []
	for _ in range(4):
		ins.append(int(input()))
	n, k, x, y = ins
	if n - k and n > k:
		print(x*k + y*(n-k))
	else:
		print(x*n)
        
resolve()