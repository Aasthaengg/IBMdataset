import sys
input = sys.stdin.readline
A,B = [int(i) for i in input().split()]
p = A + B
m = A - B
b = A* B
print(max(p,m,b))