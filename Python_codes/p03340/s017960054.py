N=int(input())
A=list(map(int,input().split()))


def ch(x,y):
    lx=len(bin(x))-2
    ly=len(bin(y))-2
    L=min(lx,ly)
    for i in range(L):
        if (x&1) and (y&1):
            return False
        x=x>>1
        y=y>>1
    return True

ans=0
temp=0
l=0
for i in range(N):
    if ch(temp,A[i]):
        temp+=A[i]
        L=i+1-l
        ans+=L
    else:
        while not (ch(temp,A[i])):
            temp-=A[l]
            l+=1
        temp+=A[i]
        L=i+1-l
        ans+=L


print(ans)
        






