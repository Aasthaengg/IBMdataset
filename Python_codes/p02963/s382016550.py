S=int(input())

if S<10**18:
    X1,Y1=0,0

    mod=10**9

    X2=mod
    Y3=S//mod + 1

    Y2=1
    X3=mod-S%mod
else:
    X1,Y1,X2,Y3=0,0,0,0
    Y2=10**9
    X3=10**9

print(X1,Y1,X2,Y2,X3,Y3)
