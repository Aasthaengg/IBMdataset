n=int(raw_input())
x=map(float,raw_input().split())
y=map(float,raw_input().split())
for p in [1,2,3]:
    d=sum([abs(x[i]-y[i])**p for i in xrange(len(x))])**(1.0/p)
    print '%6f' %(d)
print '%6f' %max([abs(x[i]-y[i]) for i in xrange(len(x))])