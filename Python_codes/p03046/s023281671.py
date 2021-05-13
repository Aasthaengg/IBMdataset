def solve(m,k):
    n=2**m
    if k>n-1:
        return [-1]
    if k==0:
        Ret=[]
        for i in range(n):
            Ret.append(i); Ret.append(i)
        return Ret
    if m==1:
        return [-1]
    Used=[False]*n
    Used[0]=True; Used[k]=True
    Pair=[]
    for i in range(1,n):
        if Used[i]:
            continue
        Pair.append([i,k^i])
        Used[i]=True; Used[k^i]=True
    A=[]
    for a,b in Pair:
        A.append(a); A.append(b)
    Ret=A+[0,k,0]+A[::-1]+[k]
    return Ret

m,k=map(int,input().split())
Ans=solve(m,k)
print(*Ans)