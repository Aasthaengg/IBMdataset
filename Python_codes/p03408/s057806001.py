import sys
input = sys.stdin.readline

N=int(input())
pts = dict()
for _ in range(N):
    s = input().strip()
    if not pts.get(s):
        pts[s] = 0
    pts[s] += 1

M=int(input())
for _ in range(M):
    t = input().strip()
    if not pts.get(t):
        pts[t] = 0
    pts[t] -= 1

print(max(0, max(pts.values())))