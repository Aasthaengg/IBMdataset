import sys
input = sys.stdin.readline

L = list(map(int, input().split()))
L.sort()
A, B, C = L

ans = 0
if (A * B * C) % 2 != 0:
    ans = A*B
print(ans)
