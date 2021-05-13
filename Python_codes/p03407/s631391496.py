import sys
input = sys.stdin.readline
A,B,C = [int(i) for i in input().split()]
if A + B >= C :
    print("Yes")
else :
    print("No")