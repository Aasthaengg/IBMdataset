import math
A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())
D = abs(A - B)
D2 = (V - W) * T
print("YES" if D <= D2 else "NO")