n,k=map(int,input().split())
if k>(n-1)*(n-2)//2:
    print(-1)
else:
    P=(n-1)*(n-2)//2-k
    counter=0
    lists=[]
    for i in range(2,n+1):
        lists.append((1,i))

    for j in range(2,n+1):
        for K in range(j+1,n+1):
            lists.append((j,K))
    lists=lists[:n-1+P]
    print(len(lists))
    for some in lists:
        print(some[0],some[1])

