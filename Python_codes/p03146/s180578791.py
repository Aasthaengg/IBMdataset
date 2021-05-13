s=int(input())

if s==1 or s==2:
    print(4)
else:
    K=1
    while s!=1:
        if s%2:
            s=3*s+1
        else:
            s//=2
        K+=1
    print(K+1)
