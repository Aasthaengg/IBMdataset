a,b,c = map(int,raw_input().split())
print len(filter(lambda x:c % x == 0,range(a,b+1)))