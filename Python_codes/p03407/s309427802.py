import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())
if A+B >= C:
    print("Yes")
else:
    print("No")