N,A,B=map(int,input().split())
if N>=2:
    if A<=B:
        print(B*(N-1)+A-(A*(N-1)+B)+1)
    else:
        print(0)
else:
    if A==B:
        print(1)
    else:
        print(0)