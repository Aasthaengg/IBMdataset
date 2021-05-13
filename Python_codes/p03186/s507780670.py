A,B,C = map(int,input().split())

if B >= C:
    print(B+C)
else:
    if A >= (C-B)-1:
        print(B+C)
    else:
        print(2*B+A+1)