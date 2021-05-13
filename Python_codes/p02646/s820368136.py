import sys

A, V = map(int, sys.stdin.readline().split())
B, W = map(int, sys.stdin.readline().split())
T = int(sys.stdin.readline())

if W < V and abs(A - B) <= (V - W) * T:
    print("YES")
else:
    print("NO")