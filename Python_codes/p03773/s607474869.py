import sys
A,B = map(int,input().split())
if A < 0 or A > 24 or B < 0 or B > 24:
    sys.exit()

start = A + B
if start > 24:
    start = start - 24
if start == 24:
    start = 0
print(start)