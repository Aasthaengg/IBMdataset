a,b,c=map(int,raw_input().split())
l=[i for i in xrange(a,b+1) if c%i==0]
print len(l)