import sys
N=int(input())
for h in range(1,3501):
    for n in range(1,h):
        a = h*n*N
        b = -(n+h)*N + 4*h*n
        if b !=0:
            if a % b ==0 and a*b>0:
                print(h,n,a//b)
                sys.exit()