import sys
input = sys.stdin.readline
A, B, C, D = map(int,input().split())
AB = A+B
CD = C+D
if AB >= CD:
    if AB > CD:
        print("Left")
    else:
        print("Balanced")
else:
    print("Right")