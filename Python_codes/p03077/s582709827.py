import math
N=int(input())
A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())

small=min(A,B,C,D,E)
if small>=N:
    print(5)
else:
    print(4+math.ceil(N/small))
