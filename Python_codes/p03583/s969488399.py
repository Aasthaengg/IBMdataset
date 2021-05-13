import sys

N = int(input())

for h in range(3500):
    h += 1

    for n in range(3500):
        n += 1

        if (4*h*n - N*n - N*h) > 0 and (N*h*n) % (4*h*n - N*n - N*h) == 0 :
            w = (N*h*n) // (4*h*n - N*n - N*h)

            print (h,n,w)
            sys.exit()
