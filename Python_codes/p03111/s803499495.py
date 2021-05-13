[N,A,B,C] = list(map(int,input().split()))
L = []
for i in range(N):
    L.append(int(input()))

import itertools
cases = list(itertools.product([0,1,2,3], repeat=N))

out = float("inf")

for case in cases:
    As =[]
    Bs =[]
    Cs =[]
    for i in range(N):
        if case[i]==1:
            As.append(i)
        if case[i]==2:
            Bs.append(i)
        if case[i]==3:
            Cs.append(i)
    LA, LB, LC = len(As),len(Bs),len(Cs)
    if LA*LB*LC==0:
        continue
    point = (LA-1)*10 + (LB-1)*10 + (LC-1)*10

    Ah = 0
    for take in As:
        Ah+=L[take]
    Bh = 0
    for take in Bs:
        Bh+=L[take]
    Ch = 0
    for take in Cs:
        Ch+=L[take]
    point += abs(A-Ah) + abs(B-Bh) + abs(C-Ch)

    if point < out:
        out = point

print(out)
