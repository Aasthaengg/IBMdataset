m,k=map(int,input().split())
if k>2**m-1 or m==k==1:
    print(-1)
elif k:
    a=[]
    for i in range(2**m):
        if i!=k:
            a.append(i)
    a.append(k)
    for i in range(2**m-1,-1,-1):
        if i!=k:
            a.append(i)
    a.append(k)
    print(*a)
else:
    a=[]
    for i in range(2**m):
        a.extend([i,i])
    print(*a)