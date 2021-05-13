a,b,c=map(int,raw_input().split())
i=0
for x in xrange(a,b+1):
    if c%x==0: i+=1
print i