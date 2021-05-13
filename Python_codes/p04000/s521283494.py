from collections import defaultdict
import sys
input = sys.stdin.readline

H, W, N = map(int, input().split())
count = defaultdict(int)
for _ in range(N):
    a, b = map(int, input().split())
    for da in range(3):
        for db in range(3):
            na, nb = a - da, b - db
            if 1 <= na <= H - 2 and 1 <= nb <= W - 2:
                count[(na, nb)] += 1
ans = [0] * 10
for k, v in count.items():
    ans[v] += 1
ans[0] = (H-2) * (W-2) - sum(ans)
print(*ans, sep='\n')
