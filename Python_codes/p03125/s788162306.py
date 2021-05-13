INPUT = list(map(int,input().split()))
A=INPUT[0]
B=INPUT[1]
if B%A == 0:
    print(A+B)
else:
    print(B-A)

