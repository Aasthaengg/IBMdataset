from collections import defaultdict
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
e = defaultdict(list)
for _ in range(n):
    t, d = map(int, input().split())
    t -= 1
    e[t].append(d)

tops = []
rests = []
for l in e.values():
    for i, d in enumerate(sorted(l, reverse=True)):
        if i == 0:
            tops.append(d)
        else:
            rests.append(d)

tops.sort(reverse=True)
c_tops = [0]
for t in tops:
    c_tops.append(c_tops[-1] + t)

rests.sort(reverse=True)
c_rests = [0]
for t in rests:
    c_rests.append(c_rests[-1] + t)

ans = 0
for i in range(1, min(k, len(tops)) + 1):
    if k - i > len(rests): continue
    ans = max(ans, c_tops[i] + c_rests[k - i] + pow(i, 2))
print(ans)
