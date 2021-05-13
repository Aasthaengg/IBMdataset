from math import ceil
from collections import deque
N, D, A = map(int, input().split())
Monsters = sorted([list(map(int, input().split())) for i in range(N)])
Monsters = [[x, ceil(h / A)] for x, h in Monsters]


acc_damage = 0
que = deque([])

ans = 0
for x, h in Monsters:
    while que and x > que[0][0]:
        limit, damage = que.popleft()
        acc_damage -= damage

    need = max(0, h - acc_damage)
    ans += need
    acc_damage += need

    if need:
        que.append([x + 2 * D, need])

print(ans)