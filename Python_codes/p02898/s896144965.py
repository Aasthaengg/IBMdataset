import sys

N, K = map(int, sys.stdin.readline().split())
H = map(int, sys.stdin.readline().split())

ans = 0
for h in H:
    if h >= K:
        ans += 1

print(ans)