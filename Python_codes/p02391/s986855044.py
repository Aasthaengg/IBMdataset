a,b=map(int,raw_input().split())
if a<-10000 or a>10000 or b<-10000 or b>10000:
    pass
elif a>b:
    print "a > b"
elif a<b:
    print "a < b"
elif a==b:
    print "a == b"