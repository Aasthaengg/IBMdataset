import sys
from collections import deque
sys.setrecursionlimit(10**9)

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N - 1)]
C = list(map(int, input().split()))

score = sum(C) - max(C)
C.sort(reverse=True)
C = deque(C)
con = [[] for _ in range(N + 1)]
ans = [0 for i in range(N + 1)]

for ab in AB:
    a, b = ab
    con[a].append(b)
    con[b].append(a)


def dfs(x):
    if len(C) == 0:
        return
    if ans[x] == 0:
        ans[x] = C[0]
        C.popleft()
        for c in con[x]:
            dfs(c)


dfs(1)
ans = list(map(str, ans))
print(score)
print(' '.join(ans[1:]))
