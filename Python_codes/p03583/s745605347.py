n=int(input())
for i in range(1,3501):
    for j in range(1,3501):
        t1=n*i*j
        t2=4*i*j-n*j-n*i
        if t2>0 and t1%t2==0:
            print(i,j,t1//t2)
            exit()