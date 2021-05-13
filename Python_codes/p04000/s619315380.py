import sys
input = sys.stdin.readline
from collections import defaultdict
H, W, N = map(int, input().split())
cnt = defaultdict(lambda : 0)
for i in range(N):
    a, b = map(lambda x: int(x)-1, input().split())
    for y in range(a-2, a+1):
        for x in range(b-2, b+1):
            if 0 <= y < H-2 and 0 <= x < W-2:
                cnt[(y, x)] += 1
ans = [0] * 10
for key in cnt:
    ans[cnt[key]] += 1
ans[0] += ans[0] + (H-2) * (W-2) - len(cnt)
for i in ans:
    print(i)
