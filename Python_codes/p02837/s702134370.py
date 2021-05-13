import sys
N = int(input())
P = [[] for _ in range(N)]
for i in range(N):
    a = int(input())
    for _ in range(a):
        x, y = map(int, sys.stdin.readline().split())
        P[i].append((x - 1, y))

ans = 0
for pattern in range(1 << N):
    ok = True
    count = 0
    for i in range(N):
        if pattern & (1 << i):
            count += 1
            for x, y in P[i]:
                if y == 1:
                    if not pattern & (1 << x):
                        ok = False
                        break
                else:
                    if pattern & (1 << x):
                        ok = False
                        break
        if not ok:
            break
    if ok:
        ans = max(ans, count)
print(ans)