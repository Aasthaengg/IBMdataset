import sys
input = sys.stdin.readline

A,B,C = sorted(list(map(int,input().split())))
print(C if A==B else A)
