
import sys
write = sys.stdout.write

while True:
    entry = map(int, raw_input().split())
    H = entry[0]
    W = entry[1]
    if H == 0 and W == 0:
        break
    
    for j in range(H):
        for k in range(W):
            if (j + k) % 2 == 0:
                write("#")
            else:
                write(".")
        print ""
    print ""