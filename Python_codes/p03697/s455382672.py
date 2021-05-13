import sys
input = sys.stdin.readline
A, B = map(int, input().split())
if A + B > 9:
  print("error")
else: print(A + B)