import sys

while True:
    h,w = map(int,raw_input().split())
    if h == 0 and w == 0:
	    break

    for i in range(h):
        for j in range(w):
    	    if (i + j) % 2 == 0:
    		    sys.stdout.write('#')
    	    else:
    		    sys.stdout.write('.')
        print''
    print