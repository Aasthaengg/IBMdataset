from collections import defaultdict, Counter, namedtuple, deque
import itertools
import functools
import bisect
import heapq
import math
from fractions import gcd

NN = 202020
MOD = 10**9+7
INF = float("inf")

n, d, a = map(int, input().split())

monsters = []
for i in range(n):
    x, h = map(int, input().split())
    monsters.append((x, h))

monsters.sort()

attack = 0
que = deque([])
attack_num = 0

for monster in monsters:
    xx, hh = monster
    while que and que[0][0] < xx - d:
        attack -= que[0][1]
        que.popleft()

    # print("a", x, h, attack, que)

    if hh - attack <= 0:
        continue

    a_times = (hh - attack - 1) // a + 1
    attack_num += a_times
    attack += a_times * a
    que.append((xx + d, a_times * a))

    # print("b", attack, attack_num, que)

print(attack_num)