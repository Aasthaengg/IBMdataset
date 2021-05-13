import sys
N = int(input())
for h in range(1,3501):
    for n in range(1,3501):
        if 4*h*n-N*n-N*h != 0:
            w,r = divmod(N*h*n,4*h*n-N*n-N*h)
            if r == 0 and w > 0:
                print(h,n,w)
                sys.exit()