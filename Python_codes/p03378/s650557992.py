def toll(n, x, tolls):
	rcount = 0
	lcount = 0
	for i in range(x, n):
		if i in tolls:
			rcount += 1
	for i in range(1, x):
		if i in tolls:
			lcount += 1
	return min(rcount, lcount)
n, m, x = map(int, input().split())
tolls = list(map(int, input().split()))
print(toll(n, x, tolls))