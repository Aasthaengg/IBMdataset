A,B,C,D=[int(input()) for _ in range(4)]
if A>B:
    if C>D:
        print(B+D)
    else:
        print(B+C)
else:
    if C>D:
        print(A+D)
    else:
        print(A+C)