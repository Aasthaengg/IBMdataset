a1=input()
res=[i for i in a1.split()]
K,X=[float(res[i]) for i in (0,1)]
k,x=K.is_integer(),X.is_integer()
if k and x == True and 1<=K<=100 and 0<=X<=100:
    K,X=int(K),int(X)
    a=X-K+1
    b=X+K-1
    if -1000000<=(a and b)<=1000000:
        for i in range(a,b+1):
            print(i,end=' ')