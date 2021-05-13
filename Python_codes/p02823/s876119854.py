N, A, B = map(int, input().split())
if (A-B)%2:
    if A > B:
        A, B = B, A
    a = (B-A-1)//2+A
    b = (B-A-1)//2+N-B+1
    print(min(a, b))
else:
    print(abs(A-B)//2)