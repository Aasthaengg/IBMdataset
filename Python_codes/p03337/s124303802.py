import sys
input = sys.stdin.readline
A, B = map(int, input().split())
li = [A+B, A-B, A*B]
print(max(li))