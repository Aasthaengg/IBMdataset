import sys
input = sys.stdin.readline
A,B,C = [int(i) for i in input().split()]
if A<=C<=B :
    print("Yes")
else :
    print("No")