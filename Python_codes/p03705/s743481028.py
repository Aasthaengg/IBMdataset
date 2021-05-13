N,A,B=map(int, input().split())

if A>B:
    print(0)
    exit()
elif N==1 and A!=B:
    print(0)
    exit()

mn=A*(N-1) + B
mx=A + B*(N-1)
print(mx-mn+1)
