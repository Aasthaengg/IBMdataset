N = int(input())
P = [int(p) for p in input().split()]
Q = [int(q) for q in input().split()]

import itertools

if P == Q:
    print(0)
else:
    perm = [i for i in range(1, N+1)]

    count = 0
    numlst = []
    for v in itertools.permutations(perm, N):
        count += 1
        if tuple(P) == v or tuple(Q) == v:
            numlst.append(count)

    print(abs(numlst[1] - numlst[0]))