import sys

sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]

    route = []
    for h in range(H):
        if h % 2 == 1:
            route.extend([(h, w) for w in range(W)])
        else:
            route.extend([(h, w) for w in reversed(range(W))])

    ans = []
    # ex. for (i1, j1), (i2, j2) in zip(route, route[1:]):
    for (i1, j1), (i2, j2) in zip(route, route[1:]):
        if A[i1][j1] % 2 == 1:
            A[i1][j1] -= 1
            A[i2][j2] += 1
            ans.append((i1 + 1, j1 + 1, i2 + 1, j2 + 1))

    print(len(ans))
    print('\n'.join(' '.join(map(str, line)) for line in ans))


resolve()