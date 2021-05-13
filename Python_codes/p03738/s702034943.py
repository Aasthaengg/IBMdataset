import sys
A = int(input())
B = int(input())

if A < 0 or A > 10 ** 100 or B < 0 or B > 10 ** 100:
    sys.exit()

if A - B > 0:
    print("GREATER")
if A - B == 0:
    print("EQUAL")
if A - B < 0:
    print("LESS")