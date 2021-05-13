N=int(input())

for h in range(1,3501):
    for n in range(1,3501):
        if 4*n*h>N*(h+n) and N*n*h%(4*n*h-N*(h+n))==0:
            w=N*n*h//(4*n*h-N*(h+n))
            print('{} {} {}'.format(h,n,w))
            exit(0)