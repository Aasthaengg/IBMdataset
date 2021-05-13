MOD=1000000007
n,k=map(int,input().split())
a=[int(i) for i in input().split()]
pos=[]
neg=[]
nzero=0
for i in a:
    if i>0:
        pos.append(i)
    elif i<0:
        neg.append(-i)
    else:
        nzero+=1
if nzero+k>n:
    print(0)
elif nzero+k==n and len(pos)>0 and len(neg)>0:
    if nzero==0:
        res=1
        for i in pos+neg:
            res*=i
            res%=MOD
        if len(neg)%2:
            res*=-1
            res+=MOD
        print(res)
    elif len(neg)%2:
        print(0)
    else:
        res=1
        for i in pos+neg:
            res*=i
            res%=MOD
        print(res)
elif len(pos)==0:
    res=1
    if k%2 and nzero>0:
        print(0)
    elif k%2:
        neg.sort()
        for i in range(k):
            res*=MOD-neg[i]
            res%=MOD
        print(res)
    else:
        neg.sort(reverse=True)
        for i in range(k):
            res*=MOD-neg[i]
            res%=MOD
        print(res)
elif len(neg)==0:
    res=1
    pos.sort(reverse=True)
    for i in range(k):
        res*=pos[i]
        res%=MOD
    print(res)
else:
    pos.sort(reverse=True)
    neg.sort(reverse=True)
    ruip=[1 for i in range(len(pos)+1)]
    ruin=[1 for i in range(len(neg)+1)]
    for i in range(len(pos)):
        ruip[i+1]=ruip[i]*pos[i]
        ruip[i+1]%=MOD
    for i in range(len(neg)):
        ruin[i+1]=ruin[i]*neg[i]
        ruin[i+1]%=MOD
    np=0
    if len(pos)>=k:
        np=k
    elif (k-len(pos))%2:
        np=len(pos)-1
    else:
        np=len(pos)
    while np>=2 and (pos[np-1]*pos[np-2]<neg[k-np+1]*neg[k-np]):
        np-=2
        if len(neg)-1<k-np+1:
            break
    print((ruip[np]*ruin[k-np])%MOD)
