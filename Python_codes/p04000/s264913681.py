from collections import defaultdict
import sys
input = sys.stdin.readline

h, w, n = map(int, input().split())
d = defaultdict(int)
dx = [1, 1, 1, 0, 0, 0, -1, -1, -1]
dy = [1, 0, -1, 1, 0, -1, 1, 0, -1]
for i in range(n):
    a, b = map(int, input().split())
    for k in range(9):
        na = a+dx[k]
        nb = b+dy[k]
        if na <= 1 or nb <= 1 or na > h-1 or nb > w-1:
            continue
        d[(na, nb)] += 1

ans = [0] * 10
for key in d:
    ans[d[key]] += 1
ans[0] = (h-2) * (w-2) - sum(ans)

for ans_i in ans:
    print(ans_i)
