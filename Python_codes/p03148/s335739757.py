import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, K = lr()
TD = [lr() for _ in range(N)]
TD.sort(key=lambda x: x[1], reverse=True)
used = set()
overlap = []
for t, d in TD[:K]:
    if t in used:
        overlap.append(d)
    else:
        used.add(t)

delicious = sum([x[1] for x in TD[:K]])
answer = delicious + len(used) ** 2
for i in range(K, N):
    if not overlap:
        break
    if TD[i][0] in used:
        continue
    delicious += (TD[i][1] -  overlap.pop())
    used.add(TD[i][0])
    if answer < delicious + len(used)**2:
        answer = delicious + len(used)**2

print(answer)
# 30