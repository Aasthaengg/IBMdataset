def solve():
    N, T = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    A.sort()
    for c,t in A:
        if t<=T:
            return c
    return 'TLE'
print(solve())