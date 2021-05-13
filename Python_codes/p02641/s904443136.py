X,N=map(int,input().split())
p=list(map(int,input().split()))
for i in range(X+1):
    for j in [-1,1]:
        a=X+j*i
        if a not in p:
            print(a)
            exit()