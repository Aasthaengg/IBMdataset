from heapq import heappop, heappush

N, C, *STC = map(int, open(0).read().split())

A = [[] for _ in range(C + 1)]
for s, t, c in zip(*[iter(STC)] * 3):
    A[c].append((s, t))

ST = []
for a in A:
    if not a:
        continue
    a = sorted(a)
    B = [a[0]]
    for s2, t2 in a[1:]:
        s1, t1 = B[-1]
        if t1 == s2:
            B[-1] = (s1, t2)
        else:
            B.append((s2, t2))
    ST += B

ST.sort(key=lambda x: x[0])

ans = 0
Q = []
for s, t in ST:
    while Q and Q[0] < s:
        heappop(Q)
    heappush(Q, t)
    ans = max(ans, len(Q))

print(ans)