A,B,C = (int(i) for i in input().split())
D = 0
if C >A+B+1:
    print(A+2*B+1)
else:
    print(B+C)