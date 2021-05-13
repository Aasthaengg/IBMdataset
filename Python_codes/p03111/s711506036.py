import itertools
n, a, b, c = map(int, input().split())
l = [int(input()) for _ in range(n)]
pat = list(itertools.product([0, 1, 2, 3], repeat=n))
ans = 10**10
for p in pat:
    aa, bb, cc = 0, 0, 0
    mp = -30
    for i in range(n):
        if p[i] == 0:
            pass
        elif p[i] == 1:
            aa += l[i]
            mp += 10
        elif p[i] == 2:
            bb += l[i]
            mp += 10
        else:
            cc += l[i]
            mp += 10
    if aa == 0 or bb == 0 or cc == 0:
        continue
    abc = [aa, bb, cc]
    pat2 = list(itertools.permutations([0, 1, 2]))
    for q in pat2:
        mp2 = 0
        mp2 += abs(a - abc[q[0]])
        mp2 += abs(b - abc[q[1]])
        mp2 += abs(c - abc[q[2]])
        ans = min(ans, mp + mp2)
print(ans)