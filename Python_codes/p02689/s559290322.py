N, M = map(int, input().split(' '))
H = list(map(int, input().split(' ')))
table = [1 for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split(' '))
    Ah, Bh = H[A - 1], H[B - 1]

    if Ah >= Bh:
        table[B - 1] = 0
    if Ah <= Bh:
        table[A - 1] = 0

ans = table.count(1)

print(ans)