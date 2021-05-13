import itertools

N, K = map(int, input().split())
A = list(map(int, input().split()))
m = 10 ** 9 + 7

internal = 0
for a0, a1 in itertools.combinations(A, 2):
    if a0 > a1:
        internal += 1

external = 0
for a0, a1 in itertools.permutations(A, 2):
    if a0 > a1:
        external += 1

ans = internal * K + external * K * (K - 1) // 2
ans = int(ans) % m
print(ans)