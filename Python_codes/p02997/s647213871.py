import itertools
n,k=map(int,input().split())

if k>(n-1)*(n-2)//2:
    print(-1)
else:
    c=(n-1)*(n-2)//2-k
    print(n-1+c)
    for i in range(1,n):
        print(i,n)
    for a,b in itertools.combinations(range(1,n),2):
        if c==0:
            break
        print(a,b)
        c-=1