from heapq import heappush, heappop
import sys

input = sys.stdin.buffer.readline


n, q = map(int, input().split())
STX = [list(map(int, input().split())) for _ in range(n)]
task = []
for s, t, x in STX:
    task.append((t - x, 0, x))
    task.append((s - x, 1, x))
for i in range(q):
    d = int(input())
    task.append((d, 2, i))

task.sort()
kouho = set()
kouho_hp = []
ans = [-1] * q
for a, b, c in task:
    if b == 0:
        kouho.remove(c)
    if b == 1:
        kouho.add(c)
        heappush(kouho_hp, c)
    if b == 2:
        while kouho_hp and kouho_hp[0] not in kouho:
            heappop(kouho_hp)
        if not kouho_hp:
            continue
        else:
            ans[c] = kouho_hp[0]
        # heapは0-indexが最小値になっているからheapified_list[0]でもよい
print(*ans, sep="\n")
