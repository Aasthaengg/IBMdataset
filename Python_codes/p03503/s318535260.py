import itertools

N = int(input())
F = [tuple(map(int, input().split())) for _ in range(N)]
P = [tuple(map(int, input().split())) for _ in range(N)]

it = itertools.product((0, 1), repeat=10)
next(it)

ans = -float('inf')
for t in it:
    p_sum = 0
    for i in range(N):
        c = sum(F[i][x] * t[x] for x in range(10))
        p_sum += P[i][c]
    ans = max(ans, p_sum)

print(ans)
