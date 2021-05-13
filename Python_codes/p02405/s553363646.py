import sys

k = 0

while k == 0:
    r = raw_input()
    H, W = r.split()
    H = int(H)
    W = int(W)
    
    if H == 0 and W == 0:
        k = 1
    else:
        for i in range(H):
            for j in range(W):
                if (i+j)%2 == 0:
                    sys.stdout.write("#")
                else:
                    sys.stdout.write(".")
            print ("")
        print("")