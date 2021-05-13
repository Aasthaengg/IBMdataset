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
	d = "#"
        for x in xrange(w-2):
            c = c + "#"
	    d = d + "."
	c += "#"
	d += "#"
        for x in xrange(h):
	    if x == 0 or x == h-1: 
		print c
	    else:
		print d
    print 