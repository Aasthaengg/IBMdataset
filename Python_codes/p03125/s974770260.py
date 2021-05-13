A,B = map(int,input().split())
if B%A == 0:
    print(A+B)
elif B%A != 0:
    print(B-A)
else:
    pass