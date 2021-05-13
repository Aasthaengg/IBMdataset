from itertools import accumulate
N, C = map(int, input().split())
R = [0] * (10**5+1)
RC = [[] for _ in range(C)]
for _ in range(N):
    s, t, c = map(int, input().split())
    RC[c-1].append((s,t))

for rc in RC:
    rc.sort()
    pt = 0
    for s, t in rc:
        if s == pt:
            R[pt] += 1
        else:
            R[s-1] += 1
        R[t] -= 1
        pt = t
print(max(list(accumulate(R))))