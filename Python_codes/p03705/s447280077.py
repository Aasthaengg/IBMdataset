N,A,B=map(int,input().split())

nin=A*(N-1)+B
nax=A+B*(N-1)

if N==1 and A!=B:
    print(0)
    exit()
elif N==1:
    print(1)
    exit()
elif A>B:
    print(0)
    exit()
print(nax-nin+1)