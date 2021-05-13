K,A,B = map(int,input().split())
if B-A<=2:
    print(1+K)
else:
    if K<=A-1:
        print(1+K)
    else:
        d = K-(A-1)
        if d==1:
            print(A+1)
        elif d%2==0:
            print(B+((d-2)//2)*(B-A))
        else:
            print(B+((d-3)//2)*(B-A)+1)