N=int(input())

for h in range(1,3501):
    for n in range(1,3501):
        x=4*n*h-n*N-h*N
        if x==0:
            continue
        w=h*n*N/x
        if w<=0:
          continue
        if N/int(w)+N/h+N/n==4:
            print(n,h,int(w))
            exit()