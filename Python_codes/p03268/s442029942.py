n,k=map(int,input().split())
if k%2==1:
    print((n//k)**3)
else:
    kk=k//2
    cnt=0
    for i in range(1,n+1):
        if i%k==kk:
            cnt+=1
    print((n//k)**3+cnt**3)