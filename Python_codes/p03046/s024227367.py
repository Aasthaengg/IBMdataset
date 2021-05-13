m,k=map(int,input().split())
m=2**m
if k>=m:
    print("-1")
elif m==1:
    if k==0:
        print("0 0")
    else:
        print("-1")
elif m==2:
    if k==0:
        print("0 0 1 1")
    else:
        print("-1")
else:
    for i in range(m):
        if i==k:
            continue
        print(i,end=" ")
    print(k,end=" ")
    for i in range(m):
        if m-1-i==k:
            continue
        print(m-1-i,end=" ")
    print(k)