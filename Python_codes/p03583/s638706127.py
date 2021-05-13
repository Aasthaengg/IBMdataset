N=int(input())
for h in range(1,3501):
    for n in range(1, 3501):
        A=4*h*n-N*n-N*h
        B=N*h*n
        if A>0:
            if B%A==0:
                print(h,n,B//A)
                break
    else:
        continue
    break