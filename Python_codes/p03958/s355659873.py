K,T=map(int,input().split())
A=list(map(int,input().split()))

B=max(A)

if T==1:
    print(K-1)
    exit()

if K%2:
    X=(K+1)//2
    if X>=B:
        print(0)
    else:
        C=B-X
        print(2*C)
else:
    Y=K//2
    if Y>=B:
        print(0)
    else:
        C=B-Y
        print(2*C-1)
