import itertools
N, M = [int(_) for _ in input().split()]
KS = [[int(_) - 1 for _ in input().split()] for _ in range(M)]
P = [int(_) for _ in input().split()]
ans = 0
for switches in itertools.product(range(2), repeat=N):
    f = all(
        sum(switches[s] for s in ks[1:]) % 2 == P[i]
        for i, ks in enumerate(KS))
    ans += f
print(ans)
