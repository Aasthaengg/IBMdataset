import math
A,B,C = map(int,input().split())

if (B/A)>=C:
    print(C)
elif (B/A)<C:
    print(math.floor(B/A))