n, C = map(int, input().split())
cq = [[] for _ in range(C)]
stc = [tuple(map(int, input().split())) for _ in range(n)]
stc = sorted(stc, key=lambda x: x[0])

for s, t, c in stc:
    c -= 1
    if cq[c]:
        fs, ft = cq[c][-1]
        if ft != s:
            cq[c].append([s, t])
        else:
            cq[c][-1] = [fs, t]
    else:
        cq[c].append([s, t])

R = [0] * (2*10**5+2)
for qq in cq:
    for s, t in qq:
        R[2*s-1] += 1
        R[2*t+1] -= 1

from itertools import accumulate
CR = list(accumulate(R))
print(max(CR))
