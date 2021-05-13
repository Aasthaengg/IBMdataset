m,k=map(int,input().split())
if 2**m<=k or m==1 and k!=0:
    print(-1)
elif m==1 and k==0:
    print(0,0,1,1)
else:
    ans=[k]
    for i in range(2**m):
        if i!=k:
            ans.append(i)
    ans.append(k)
    for i in range(2**m):
        i=2**m-1-i
        if i!=k:
            ans.append(i)
    print(*ans)