import itertools

N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]

ans = float('inf')
for Lp in itertools.permutations(L):
    Lac = tuple(itertools.accumulate(([0] + list(Lp))))
    for a in range(1, N - 1):
        for b in range(a + 1, N):
            for c in range(b + 1, N + 1):
                A_MP = 10 * (a - 1) + abs(Lac[a] - Lac[0] - A)
                B_MP = 10 * (b - a - 1) + abs(Lac[b] - Lac[a] - B)
                C_MP = 10 * (c - b - 1) + abs(Lac[c] - Lac[b] - C)
                ans = min(ans, A_MP + B_MP + C_MP)
print(ans)
