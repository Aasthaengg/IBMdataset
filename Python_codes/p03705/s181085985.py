N,A,B=map(int,input().split())

if A>B:
    print(0)
elif N==1 and A<B:
    print(0)
elif N==1 and A==B:
    print(1)
elif N==2:
    print(1)
else:
    print(A+B*(N-1)-(A*(N-1)+B)+1)