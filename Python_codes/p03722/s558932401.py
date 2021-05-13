def solve(n, m, ABC):
    distance = [None] * n
    distance[0] = 0

    for _ in range(n - 1):
        for a, b, c in ABC:
            if distance[a - 1] is None:
                continue
            if distance[b - 1] is None or distance[b - 1] < distance[a - 1] + c:
                distance[b - 1] = distance[a - 1] + c

    for _ in range(n - 1):
        for a, b, c in ABC:
            if distance[a - 1] is None or distance[b - 1] is None:
                continue
            if distance[b - 1] < distance[a - 1] + c:
                distance[b - 1] = distance[a - 1] + c
                if b == n:
                    return 'inf'

    return distance[n - 1]

_n, _m = map(int, input().split())
_ABC = [list(map(int, input().split())) for _ in range(_m)]
print(solve(_n, _m, _ABC))
