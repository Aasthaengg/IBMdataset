
A,B,C=map(int,input().split())
if B>=C:
    print(B+C)
else:
    print(min(B+C,2*B+A+1))

