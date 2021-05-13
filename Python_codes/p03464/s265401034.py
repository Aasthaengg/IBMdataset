K = int(input())
A = list(map(int,input().split()))

minn = 2
maxn = 3
if A[-1] != 2:
	minn = -1

if minn != -1:
	for i in range(K-2,-1,-1):
		m = A[i]
		a = (minn + m - 1) // m * m
		b = maxn // m * m
		if b < a:
			minn = -1
			break
		minn = a
		maxn = b + m - 1

if minn == -1:
	print(minn)
else:
	print(minn,maxn)