N,A,B=map(int,input().split())
C=A
D=B
ans=0
a=abs(A-B)
if a%2==0:
    print(a//2)
else:
    nb=N-B
    ans+=nb
    A+=nb
    B=N
    A+=1
    ans+=1
    ab=abs(A-B)
    ans+=ab//2

    A=C
    B=D
    val=0
    na=A-1
    B=B-na
    A=1
    val+=na
    B=B-1
    #print(B)
    val+=1
    na=abs(A-B)
    #print(na)
    val+=na//2
    ans=min(ans,val)
    print(ans)