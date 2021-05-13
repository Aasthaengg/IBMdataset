import sys
input = sys.stdin.buffer.readline
P, Q, R = map(int, input().split())
ans = min(P + Q, Q + R, R + P)
print(ans)
