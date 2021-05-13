import sys
A,B,C = map(int,input().split())

if A < -100 or A > 100 or B < -100 or B > 100 or C < -100 or C > 100:
    sys.exit()

if C >= A and C <= B:
    print("Yes")
else:
    print("No")