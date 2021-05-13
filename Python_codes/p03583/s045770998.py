n=int(input())
for i in range(1,3501):
    for j in range(1,3501):
        if 4*i*j-n*(i+j)<=0:
            continue
        else:
            if (n*i*j)%(4*i*j-n*(i+j))==0:
                h=i
                N=j
                w=n*i*j//(4*i*j-n*(i+j))
                break
print(h,N,w)
