from collections import defaultdict
import sys

input = sys.stdin.buffer.readline
h, w, n = map(int, input().split())
count = defaultdict(int)
# 3＊3の左上の位置でカウント
for i in range(n):
    a, b = map(int, input().split())
    for s in range(3):
        if a + s - 2 < 1 or a + s - 2 > h - 2:
            continue
        for t in range(3):
            if b - 2 + t < 1 or b - 2 + t > w - 2:
                continue
            count[(a - 2 + s, b - 2 + t)] += 1
ans = [0] * 10
for key, val in count.items():
    ans[val] += 1
ans[0] = (h - 2) * (w - 2) - sum(ans[1:])
print(*ans, sep="\n")
