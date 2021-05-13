import sys
from operator import itemgetter
read = sys.stdin.read

N, K, *td = map(int, read().split())
td = sorted(zip(*[iter(td)] * 2), key=itemgetter(1), reverse=True)

stack = []
taste = 0
neta_group = set()
for t, d in td[:K]:
    taste += d
    if t in neta_group:
        stack.append(d)
    else:
        neta_group.add(t)

variety = len(neta_group)
candidates = [taste + variety ** 2]

if N == K:
    print(candidates[0])
    exit()

rest = list(reversed(td[K::]))

while rest and stack:
    t1, d1 = rest.pop()
    if t1 not in neta_group:
        neta_group.add(t1)
        d2 = stack.pop()
        variety += 1
        taste = taste - d2 + d1

        candidates.append(taste + variety ** 2)

print(max(candidates))