n=int(input())
A=list(map(int,input().split()))
A=sorted(A)
B=list(map(int,input().split()))
B=sorted(B)
C=list(map(int,input().split()))
C=sorted(C)
def ais_ok(i,b):
    if i<-1: #all ng ok=-1
        return True
    if n<=i: #all ok ng=n
        return False
    return A[i]<b #okになる条件
def cis_ok(i,b):
    if i<-1: #all ok ng=-1
        return False
    if n<=i: #all ng ok=n
        return True
    return b<C[i]
ans=0
for i in range(n):
    b=B[i]
    ok_a,ng_a=-1,n
    ok_c,ng_c=n,-1
    while (ng_a-ok_a)>1:
        mid=(ok_a+ng_a)//2
        if ais_ok(mid,b):
            ok_a=mid
        else:
            ng_a=mid
    while (ok_c-ng_c)>1:
        mid=(ok_c+ng_c)//2
        if cis_ok(mid,b):
            ok_c=mid
        else:
            ng_c=mid
    ans+=(ok_a+1)*(n-(ng_c+1))
print(ans)