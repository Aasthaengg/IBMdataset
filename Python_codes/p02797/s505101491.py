def resolve():
    n,k,s=map(int,input().split())
    l1=[s]*k
    if s!=10**9:
        l2=[s+1]*(n-k)
    else:
        l2=[1]*(n-k)
    print(*(l1+l2))
resolve()
