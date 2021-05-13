#ABC156 - Virtual
sel='A'
#A
if sel=='A':
    N,R=map(int,input().split())
    if N>=10:
        print(R)
    else:
        print(R+100*(10-N))
#B
if sel=='B':
    N,K=map(int,input().split())
    cnt=0
    while N>0:
        N//=K
        cnt+=1
    print(cnt)

#C
if sel=='C':
    def ceilT(a,b): #ceil(a/b)
        return (a+b-1)//b

    N=int(input())
    X=[int(i) for i in input().split()]
    p=ceilT(sum(X),N)
    ans=sum((x-p)**2 for x in X)
    p-=1
    ans=min(ans,sum((x-p)**2 for x in X))
    print(ans)




