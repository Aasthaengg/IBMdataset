m,k=map(int,input().split())
if m==1 and k==0:
    a=[0,0,1,1]
    print(*a)
    exit()
elif m==1 and k==1:
    print(-1)
    exit()
if k<=2**m-1:
    ans=[]
    for i in range(2**(m)):
        if i!=k:
            ans.append(i)
    ans.append(k)
    for i in range(2**m-1,-1,-1):
        if i!=k:
            ans.append(i)
    ans.append(k)
    print(*ans)
else:
    print(-1)
