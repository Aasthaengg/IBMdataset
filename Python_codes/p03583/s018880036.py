n=int(input())
a=n*3//4+3
for i in range(max(n//4,1),a):
    for j in range(a-3,3501):
        k=4*i*j-n*(i+j)
        if k==0:
            continue
        x,y=divmod(n*i*j,k)
        if y==0 and x>0:
            print(i,j,x)
            exit()
