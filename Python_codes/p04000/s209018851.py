import itertools
H, W, N = [int(_) for _ in input().split()]
AB = [[int(_) for _ in input().split()] for _ in range(N)]

memo = {}
for a, b in AB:
    #0-indexed
    a -= 1
    b -= 1
    for na, nb in itertools.product(range(a - 2, a + 1), range(b - 2, b + 1)):
        if na in range(H - 2) and nb in range(W - 2):
            memo[na + H * nb] = memo.get(na + H * nb, 0) + 1
result = [0] * 10
for k, v in memo.items():
    result[v] += 1
result[0] = (H - 2) * (W - 2) - sum(result)
[print(_) for _ in result]
