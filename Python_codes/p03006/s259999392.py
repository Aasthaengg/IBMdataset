N = int(input())

P = []
for _ in range(N):
    x, y = map(int, input().split())
    P.append((x, y))

from collections import defaultdict

if N == 1:
    print(1)
    exit(0)

cnt = defaultdict(int)
for pi in range(N):
    for pj in range(N):
        if pi == pj:
            continue
        # x
        dx = P[pi][0] - P[pj][0]

        # y
        dy = P[pi][1] - P[pj][1]

        cnt[(dx, dy)] += 1

ans = N-max(cnt.values())
print(ans)

