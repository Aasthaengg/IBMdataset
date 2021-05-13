from itertools import combinations

N, K = map(int, input().split())


def cmb(x):
    return x * (x - 1) // 2


if K > cmb(N - 1):
    print(-1)
else:
    m = cmb(N - 1) - K
    print(N - 1 + m)

    for i, j in list(combinations(range(1, N + 1), 2))[:N - 1 + m]:
        print(i, j)