import sys
input = sys.stdin.readline
A,B,C,D = [int(i) for i in input().split()]
if A*B>=C*D:
    print(A*B)
else :
    print(C*D)