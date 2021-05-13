import sys
input = sys.stdin.readline
A,B = [int(i) for i in input().split()]
print((A+B)%24)