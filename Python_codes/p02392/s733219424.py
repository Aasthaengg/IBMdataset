a,b,c =raw_input().split()
a,b,c = map(int,(a,b,c))
if a < b < c:
    print 'Yes'
else:
    print 'No'