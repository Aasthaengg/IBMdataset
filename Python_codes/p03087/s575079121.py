from itertools import accumulate


[N, Q], [S], *LR = [s.split() for s in open(0)]
N, Q = map(int, (N, Q))
acc = [0] + list(accumulate([S[i] + S[i + 1] == 'AC' for i in range(N - 1)]))
for l, r in LR:
    l, r = map(lambda x: int(x) - 1, (l, r))
    print(acc[r] - acc[l])
