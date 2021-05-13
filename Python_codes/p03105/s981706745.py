A,B,C = [int(i) for i in input().split()]
if A*C <= B:
    print(C)
else:
    print(B//A)