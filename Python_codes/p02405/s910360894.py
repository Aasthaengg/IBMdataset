while True:
    
    H, W = map(int, raw_input().split())

    if H == 0 and W == 0:
        break


    for i in range(H):
	    if i%2 == 0:
	        print "#." * (W/2) + "#" * (W%2)
	    else:
	        print ".#" * (W/2) + "." * (W%2)
    print ""