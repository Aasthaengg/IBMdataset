N, A, B = map(int,input().split())
if A > B:
    print(0)
    exit(0)
if N == 1:
    if A != B:
        print(0)
    else:
        print(1)
else:
    print((N-1)*B+A-(N-1)*A-B+1)
