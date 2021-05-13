N=int(input())
a=4/N
h_st=max(int(N*(1/4))-1,1)
#h_st=1
for h in range(h_st,3501):
    H=1/h
    for n in range(1,3501):
        a=(4*h*n-N*n-N*h)
        #print(h,n)
        if a:
            w=N*h*n/a
            if w>0 and w.is_integer():
                print(h,n,int(w))
                exit()

print(h,n,w)
