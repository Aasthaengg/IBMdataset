import sys

N=int(input())

for h in range(1,3*N//4+1):
    if 4*h>N:
        for n in range(1,(2*N*h)//(4*h-N)+1):
            if (4*h-N)*n>N*h:
                if (N*h*n)%((4*n*h-N*n-N*h))==0:
                    w=(N*h*n)//((4*n*h-N*n-N*h))
                    print(h,n,w)
                    sys.exit()