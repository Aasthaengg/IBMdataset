N = int(input())

F = []

for _ in range(N):
    f = list(input().strip().split())
    F.append(int("".join(f), 2))


P = [list(map(int, input().split())) for _ in range(N)]

ans = -float('inf')

for i in range(1, 2**10):
    candi = 0
    for n in range(N):
        tmp = i & F[n]
        p = format(tmp, 'b').count("1")
        candi += P[n][p]
    if candi == 0:
        foo = 1
    ans = max(ans, candi)

print(ans)
