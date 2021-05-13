import sys
from collections import Counter
import copy

n = int(sys.stdin.readline())
ct = Counter()
a_ls = dict()
for i in range(n):
    inp = [int(i) - 1 for i in sys.stdin.readline().split()]
    a_ls[i] = inp
cnt = 0
candidate = list(range(n))
rest = n * (n - 1) / 2
combis = set()
while rest:
    no_ls = []
    next_candidate = []
    flg = False
    for i in candidate:
        if len(a_ls[i]) == 0:
            continue
        target = a_ls[i][0]
        if (i, target) in combis or (target, i) in combis:
            next_candidate.append(i)
            next_candidate.append(target)
            rest -= 1
            if len(a_ls[i]) > 0:
                a_ls[i].pop(0)
            if len(a_ls[target]) > 0:
                a_ls[target].pop(0)
            flg = True
        else:
            combis.add((i, target))
    candidate = next_candidate
    if not flg:
        cnt = -1
        break
    cnt += 1
print(cnt)