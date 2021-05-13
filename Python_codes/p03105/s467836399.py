A,B,C = map(int,input().split())

if B // A >= 1:
    if C <= B // A:
        print(C)
    elif B // A < C:
        print(B // A)
else:
    print(0)