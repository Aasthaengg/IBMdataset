import sys
input = sys.stdin.readline

A=list(input().rstrip().split())
print(min(A)*int(max(A)))
