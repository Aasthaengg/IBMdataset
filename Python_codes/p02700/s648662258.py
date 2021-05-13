import math


A,B,C,D = map(int,input().split())

tk = math.ceil(C/B)
ao = math.ceil(A/D)

if tk<=ao:
    print("Yes")
else:
    print("No")