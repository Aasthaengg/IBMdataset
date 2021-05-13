import sys
X,A,B = map(int,input().split())
if X < 0 or A < 0 or B < 0 or X > 10 ** 9 or A > 10 ** 9 or B > 10 ** 9:
    sys.exit()

if B - A < X + 1 and B - X > 0:
    print("safe")
if B - A < X + 1 and B - X < 0:
    print("delicious")
if B - A >= X + 1:
    print("dangerous")
