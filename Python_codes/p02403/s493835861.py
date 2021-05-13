
import sys
write = sys.stdout.write

while True:
    entry = map(int, raw_input().split())
    H = entry[0]
    W = entry[1]
    if H == 0 and W == 0:
        break
    for i in range(H):
    	for j in range(W):
    		write("#")
    	print ""
    print ""