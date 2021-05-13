import sys
A,B = map(int,input().split())
if A < 0 or A > 10 or B < 0 or B > 10:
    sys.exit()
if A + B >= 10:
    print("error")
if A + B < 10:
    print(A + B)