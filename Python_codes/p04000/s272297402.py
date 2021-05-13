import sys
from collections import defaultdict
input = sys.stdin.buffer.readline

count = defaultdict(lambda: 0)

H, W, N = map(int, input().split())
for _ in range(N):
    a, b = map(int, input().split())
    for a_2 in range(a-1, a+2):
        for b_2 in range(b-1, b+2):
            if 2 <= a_2 <= H-1 and 2 <= b_2 <= W-1:
                count[a_2, b_2] += 1

ans = [0] * 10
for _, v in count.items():
    ans[v] += 1

ans[0] = (H-2) * (W-2) - sum(ans)

print(*ans, sep = '\n')