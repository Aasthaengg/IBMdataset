import sys
A,B = map(int,input().split())

if A < 0 or B < 0 or A > 100 or B > 100:
    sys.exit()

if A % 3 == 0 or B % 3 == 0 or (A + B) % 3 == 0:
    print("Possible")
else:
    print("Impossible")