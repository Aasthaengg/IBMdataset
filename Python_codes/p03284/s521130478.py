def LI():
	return [ int(s) for s in input().split() ]
N,K = LI()
print(1) if N % K != 0 else print(0)