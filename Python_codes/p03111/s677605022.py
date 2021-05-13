from itertools import product
N, A, B, C = map(int, input().split())
L = [int(input()) for i in range(N)]
INF = 10 ** 30
def calc(p):
    if sum(list(set(p))) < 6:
        return INF
    a, b, c = 0, 0, 0
    ac, bc, cc = 0, 0, 0
    for i, v in enumerate(p):
        if v == 1:
            a += L[i]
            ac += 1
        elif v == 2:
            b += L[i]
            bc += 1
        elif v == 3:
            c += L[i]
            cc += 1
    return abs(A-a) + abs(B-b) + abs(C-c) + (ac+bc+cc-3) * 10

ans = INF
for p in product(range(4), repeat=N):
    ans = min(ans, calc(p))
print(ans)
