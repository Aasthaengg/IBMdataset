a,b,c=map(int,raw_input().split())
if a<0 or a>100 or b<0 or b>100 or c<0 or c>100:
    pass
elif a<b<c:
    print "Yes"
else:
    print "No"