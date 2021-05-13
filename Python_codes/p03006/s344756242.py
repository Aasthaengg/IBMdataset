from collections import defaultdict
from typing import Counter

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
cnt = defaultdict(Counter)

ans = 0

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        a = XY[i][0]-XY[j][0]
        b = XY[i][1]-XY[j][1]
        cnt[a][b] += 1
        ans = max(cnt[a][b], ans)

print(N-ans)