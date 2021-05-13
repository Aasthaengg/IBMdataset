A, B = map(int,input().split())
X = 0
if A > B:
    X = A
    A -= 1
    if A > B:
        X += A
        print(X)
    else:
        X += B
        print(X)    
else:
    X = B
    B -= 1
    if A > B:
        X += A
        print(X)
    else:
        X += B
        print(X)

