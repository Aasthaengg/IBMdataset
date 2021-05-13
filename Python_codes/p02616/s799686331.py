MOD=10**9+7

def moddiv(a,m):
    return pow(a,m-2,m)

def solve():
    res=-10**30
    minus,plus,zero=[],[],[]
    for i in range(N):
        if A[i]<0:
            minus.append(A[i])
        elif A[i]>0:
            plus.append(A[i])
        else:
            zero.append(A[i])
    cump=1
    plus.sort()
    minus.sort()
    for i in range(len(plus)):
        cump=cump*plus[i]%MOD
    j=0
    i=0
    cumm=1
    while(j<=min(len(minus),K)):
        if j>0:
            cumm=cumm*minus[j-1]*minus[j-2]%MOD
            newm=minus[j-1]*minus[j-2]
        else:
            newm=0
        isbig=True
        if K-j>len(plus):
            j+=2
            continue
        oldp=1
        while(K-j<len(plus)-i):
            cump=cump*moddiv(plus[i],MOD)%MOD
            if isbig:
                oldp*=plus[i]
            if oldp>newm:
                isbig=False
            i+=1
        if j>0:
            if newm>oldp:
                res=cumm*cump%MOD
        else:
            res=max(res,cumm*cump%MOD)
        j+=2
    if res!=-10**30:
        return res
    if len(zero)>0:
        return 0
    li=minus+plus
    li.sort(key=lambda x:abs(x))
    res=1
    for i in range(K):
        res=res*li[i]%MOD
    return res
N,K=map(int,input().split())
A=list(map(int,input().split()))

if min(A)>=0:
    res=1
    A.sort(reverse=True)
    for i in range(K):
        res=res*A[i]%MOD
elif max(A)<=0:
    res=1
    if not K%2:
        A.sort()
        for i in range(K):
            res=res*A[i]%MOD
    else:
        A.sort(reverse=True)
        for i in range(K):
            res=res*A[i]%MOD
else:
    res=solve()
print(res)