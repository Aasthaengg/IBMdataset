if __name__ == '__main__':
	n,m,l=map(int,raw_input().split())
	a=[map(int,raw_input().split()) for _ in xrange(n)]
	b=zip(*[map(int,raw_input().split()) for _ in xrange(m)])
	sums=[i[k]*j[k] for i in a for j in b for k in xrange(m)]
	c=[sum(sums[i:i+m]) for i in [j for j in xrange(len(sums)) if j%m==0]]
	for i in xrange(len(c)):
		if (i+1)%l==0: print c[i]
		else: print c[i],