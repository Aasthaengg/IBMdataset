[a,b,c] = raw_input().split(' ')
a = int(a)
b = int(b)
c = int(c)
h = True
if a < b:
    if b < c:
        print 'Yes'
        h = False
        
if h:
    print 'No'