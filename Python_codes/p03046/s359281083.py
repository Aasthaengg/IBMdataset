m,k=map(int,input().split())
r=range(2**m)
if k>2**m-1or m==k==1:
    print(-1)
elif k:
    a=[i for i in r if i!=k]
    print(*a+[k]+a[::-1]+[k])
else:
    for i in r:print(i,i)