if __name__ == '__main__':
	n,m,l=map(int,raw_input().split())
	a=[map(int,raw_input().split()) for _ in [0]*n]
	b=zip(*[map(int,raw_input().split()) for _ in [0]*m])
	sums=[i[k]*j[k] for i in a for j in b for k in xrange(m)]
	c=[sum(sums[i:i+m]) for i in [j for j in xrange(len(sums)) if j%m==0]]
	c=[c[i:i+l] for i in xrange(len(c)) if i%l==0]
	for i in c:
		print " ".join(map(str, i))