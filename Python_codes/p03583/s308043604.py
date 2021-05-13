import math
N=int(input())

for h in range(1,3501):
    for n in range(1,3501):
        x,y=N*h*n,4*h*n-n*N-h*N
        if y==0:
            continue
        w=x/y
        if w>0 and math.floor(w)==math.ceil(w):
            print(h,n,math.floor(w))
            exit()