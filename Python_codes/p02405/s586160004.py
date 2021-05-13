h = []
w = []
while True:
    a,b = map(int, raw_input().split())
    h.append(a)
    w.append(b) 
    if a == 0 and b == 0:
        break

for h,w in zip(h,w):    
    if h == 0 and w == 0:
        break;
    else:
	c = "#"
	d = "."
        for x in xrange(1,w):
	    if x%2 == 1:
                c = c + "."
	        d = d + "#"
	    else:
	        c = c + "#"
	        d = d + "."

        for x in xrange(1,h+1) :
	    if x%2 == 1: 
		print c
	    else:
		print d
    print 