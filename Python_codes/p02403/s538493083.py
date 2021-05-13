import sys
k = 1

while k == 1:
    r = raw_input()
    H, W = r.split()
    H = int(H)
    W = int(W)
    
    if H == 0 and W == 0:
        k = 0
    else:
        for i in range(H):
            for j in range(W):
                sys.stdout.write("#")
            print ("")
        print("")