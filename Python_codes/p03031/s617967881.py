N, M = list(map(int, input().split()))
KS = [list(map(int, input().split())) for _ in range(M)]
P = list(map(int, input().split()))

answer = 0
from itertools import product

for sw in product([0, 1], repeat=N):
    for p, ks in zip(P, KS):
        K = ks[0]
        S = ks[1:]
        if sum([sw[s - 1] for s in S]) % 2 != p % 2:
            break
    else:
        answer += 1

print(answer)
