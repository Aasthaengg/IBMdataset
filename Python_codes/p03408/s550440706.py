def actual(N, S, M, T):
    points = [S.count(word) - T.count(word) for word in set(S)]

    return max(0, max(points))

N = int(input())
S = [input() for _ in range(N)]

M = int(input())
T = [input() for _ in range(M)]

print(actual(N, S, M, T))
