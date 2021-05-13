n = int(input())
S = input()

sapp = [[0] * n for _ in range(10)]
for idx, s in enumerate(S):
    sapp[int(s)][idx] = 1

from itertools import accumulate
sacc = [list(accumulate(sa)) for sa in sapp]

pins = set()
for i in range(1, n-1):
    for lnum in range(10):
        if sacc[lnum][i-1] == 0:
            continue
        for rnum in range(10):
            # i+1から最後までで出現するか
            rnumc = sacc[rnum][-1] - sacc[rnum][i]
            if rnumc > 0:
                pins.add(100*lnum + 10*int(S[i]) + rnum)

print(len(pins))
