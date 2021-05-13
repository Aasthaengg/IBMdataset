import sys

while(1):
    H, W = map(int, raw_input().split())
    if(H == 0 and W == 0):
        break
    else:
        for i in range(H):
            for j in range(W):
                sys.stdout.write("#")
            print
        print