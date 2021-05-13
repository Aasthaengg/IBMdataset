N=int(input())
A=list(map(int,input().split()))
MOD=10**9+7
x=dict()
y=dict()
flag=True

if N%2==0:
    for i in range(1,N,2):
        x[i]=0
    for i in range(N):
        if A[i] in x:
            x[A[i]]+=1
        else:
            y[A[i]]=1
    for idx in x:
        if idx==0:
            if x[idx]<1:
                flag=False
            continue
        if x[idx]!=2:
            flag=False
    ans=1
    if flag:
        for idx in x:
            ans=ans*x[idx]
    else:
        print(0)
        exit()
    ans=ans%MOD
    print(ans)

else:
    for i in range(0,N,2):
        x[i]=0
    for i in range(N):
        if A[i] in x:
            x[A[i]]+=1
        else:
            y[A[i]]=1
    for idx in x:
        if idx ==0:
            if x[idx]<1:
                flag=False
            continue
        if x[idx]!=2:
            flag=False
    ans=1
    if flag:
        for idx in x:
            ans=ans*x[idx]
    else:
        print(0)
        exit()
    ans=ans%MOD
    print(ans)