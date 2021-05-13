import sys
A,B,C,D = map(int,input().split())
if A > 10000 or B > 10000 or C > 10000 or D > 10000:
    sys.exit()
if A * B >= C * D:
    print(A*B)
    sys.exit()
if A * B <= C*D:
    print(C*D)
    sys.exit()