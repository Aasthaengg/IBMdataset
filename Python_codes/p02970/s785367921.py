def solve():
    N, M = map(int, input().split())
    c = 0
    r = 0
    while r < N:
        r += M*2 + 1
        c += 1

    return c

print(solve())