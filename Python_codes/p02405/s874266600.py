import sys
while 1:
    H, W = map(int, raw_input().split())
    if H == 0 and W == 0:
        break
    else:
        for j in xrange(H):
            for i in xrange(W):
                if (i + j) % 2 == 0:
                    sys.stdout.write("#")
                else:
                    sys.stdout.write(".")
            print ""
        print ""