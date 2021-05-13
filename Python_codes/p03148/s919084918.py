import os
import sys
from collections import deque
from operator import itemgetter

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353

N, K = list(map(int, sys.stdin.buffer.readline().split()))
TD = [list(map(int, sys.stdin.buffer.readline().split())) for _ in range(N)]

t_seen = [False] * (N + 1)
sushi_seen = [False] * N
TD.sort(key=itemgetter(1), reverse=True)

delicious = 0
que = deque()
for i, (t, d) in enumerate(TD):
    if len(que) >= K:
        break
    if not t_seen[t]:
        que.append(i)
        delicious += d
        t_seen[t] = True
        sushi_seen[i] = True
for i, (t, d) in enumerate(TD):
    if len(que) >= K:
        break
    if not sushi_seen[i]:
        que.appendleft(i)
        delicious += d
        sushi_seen[i] = True

idx = i
type_cnt = sum(t_seen)
ans = delicious + type_cnt ** 2
while idx < que[-1]:
    while idx < N and sushi_seen[idx]:
        idx += 1
    if idx >= N:
        break
    que.appendleft(idx)
    delicious -= TD[que.pop()][1]
    delicious += TD[idx][1]
    type_cnt -= 1
    score = delicious + type_cnt ** 2
    ans = max(ans, score)
    sushi_seen[idx] = True
print(ans)
