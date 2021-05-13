import sys
input = lambda: sys.stdin.readline().rstrip()

N, T = map(int, input().split())

ans = 10 ** 10
for i in range(N):
    c, t = map(int, input().split())
    if t <= T:
        ans = min(ans, c)

print(ans if ans != 10**10 else "TLE")