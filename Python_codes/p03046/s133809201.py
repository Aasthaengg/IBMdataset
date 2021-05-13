m,k=map(int,input().split())

if k==0:
    x=[[i]*2 for i in range(2**m)]
    for i in x:
        print(*i,end=" ")
elif m==1:
    print(-1)
elif 2**m<=k:
    print(-1)
else:
    for i in reversed(range(2**m)):
        if i!=k:
            print(i,end=" ")
    print(k,end=" ")
    for i in range(2**m):
        if i!=k:
            print(i,end=" ")
    print(k)