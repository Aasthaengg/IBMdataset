m,k=map(int,input().split())
if 0<=k<2**m:
    if m==1:
        if k==1:print(-1)
        else:print(*[1,1,0,0])
    else:
        s=[str(i) for i in range(2**m) if i!=k]
        c=""
        for i in s:c+=i+" "
        c+=str(k)+" "
        for i in s[::-1]:c+=i+" "
        print(c+str(k))
else:
    print(-1)