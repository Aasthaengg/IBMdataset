N=int(input())
A=list(map(int,input().split()))

if 0 in A:
    S=0
    for a in A:
        S+=abs(a)
    print(S)
else:
    X=0
    S=0
    for a in A:
        X+=(a<0)
        S+=abs(a)

    if X%2==0:
        print(S)
    else:
        b=abs(min(A,key=lambda x:abs(x)))
        print(S-2*b)