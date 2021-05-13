import sys
def az14():
    while True:
        xs = raw_input().split()
        H,W = int(xs[0]),int(xs[1]) 
        if H==0 and W==0 : break
        for i in range(0,H):
            for j in range (0,W):
                if (i+j)%2 == 0:
                    sys.stdout.write("#")
                else:
                    sys.stdout.write(".")
            print
        print

az14()