import sys
N, M = map(int, input().split())
ansl = 1
ansr = N
for _ in range(M):
    l, r = map(int, sys.stdin.readline().split())
    ansl = max(ansl, l)
    ansr = min(ansr, r)
ans = max(0, ansr - ansl + 1)
print(ans)