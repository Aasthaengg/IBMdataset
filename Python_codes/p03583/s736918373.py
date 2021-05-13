n = int(input())
import sys
for i in range(1, 3501):
    for j in range(1, 3501):
        w_t = n*i*j
        w_u = 4*i*j - i*n -j*n
        if w_u > 0:
            w = w_t/w_u
            if w.is_integer():
                print("%s %s %s" % (i, j, int(w)))
                sys.exit()