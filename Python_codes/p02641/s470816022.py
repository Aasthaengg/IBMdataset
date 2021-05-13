def retminabs(x,p):
    dif=0
    while True:
        if not x-dif in p:
            return x-dif
        elif not x+dif in p:
            return x+dif
        dif+=1
X,N=map(int,input().split())
P=list(map(int,input().split()))
print(retminabs(X,P))