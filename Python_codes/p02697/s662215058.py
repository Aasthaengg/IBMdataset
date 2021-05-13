N,M=map(int,input().split())
l=1
r=N
dis=set()
if N%2==1:
    for i in range(M):
        print(l,r)
        l=l+1
        r=r-1
else:
    for _ in range(M):
        print(l,r)
        a,b=r-l,N+l-r
        dis.add(a)
        dis.add(b)
        l=l+1
        r=r-1
        if r-l in dis or N+l-r in dis or r-l==N+l-r:
            r=r-1