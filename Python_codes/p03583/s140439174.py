N=int(input())
for h in range(1,3500):
    for w in range(1,3500):
        if (4*h*w-N*h-N*w)==0:continue
        if N*h*w%(4*h*w-N*h-N*w):continue
        x=N*h*w//(4*h*w-N*h-N*w)
        if x>0:
            print(h,w,x);exit()
