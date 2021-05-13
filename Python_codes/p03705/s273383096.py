N,A,B = map(int,input().split())
if N == 1:
    if A != B:
        print(0)
    else:
        print(1)
elif A == B:
    print(1)
elif A > B:
    print(0)
else:
    print(B*(N-1)+A - (A*(N-1)+B) + 1)