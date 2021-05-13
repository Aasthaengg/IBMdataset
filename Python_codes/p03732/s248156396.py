import sys
from copy import deepcopy
N, W = map(int, raw_input().split())
pre = []
V = 0
for i in range(N):
    w, v = map(int, raw_input().split())
    V += v
    pre.append((w, v))
minw = min(pre)[0]
items1 = []
items2 = []
items3 = []
items4 = []
for w, v in pre:
    if w == minw:
        items1.append((w, v))
    elif w == minw + 1:
        items2.append((w, v))
    elif w == minw + 2:
        items3.append((w, v))
    else:
        items4.append((w, v))
items1.sort(reverse=True)
items2.sort(reverse=True)
items3.sort(reverse=True)
items4.sort(reverse=True)
items = [items1, items2, items3, items4]
memo = {}

def dfs(indice, W, value):
    if W < 0:
        return -(10**9)
    if W < minw or W == 0:
        return value
    if indice in memo:
        return memo[indice]
    outOfAmmo = True
    indicel = list(indice)
    sofar = -(10**9)
    for i in range(4):
        if indice[i] < len(items[i]):
            outOfAmmo = False
            new_indice = deepcopy(indicel)
            new_indice[i] += 1
            current_item = items[i][indice[i]]
            sofar = max(sofar, dfs(tuple(new_indice), W-current_item[0], value+current_item[1]))
    memo[indice] = sofar
    if outOfAmmo:
        return value
    return sofar
print dfs((0, 0, 0, 0), W, 0)
