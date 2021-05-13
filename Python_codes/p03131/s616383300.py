K,A,B=map(int,input().split())
c=1

if A+2<B:
    if K<=A:
        print(1+K)
    else:
        K-=A-1
        c+=A-1
    #    print(c)
        if K%2:
            K-=1
            c+=1
        c+=K//2*(B-A)
        print(c)
else:
    print(1+K)
