def make_table(N=200):
    import math
    import itertools
    table = [False for _ in range(N + 1)]
    A = list(range(3, math.ceil(math.sqrt(N)), 2))
    # x^1, y^1, z^1
    for x, y, z in itertools.combinations(A, 3):
        if x * y * z <= N:
            table[x * y * z] = True
    # x^3, y^1
    for x, y in itertools.combinations(A, 2):
        if x * x * x * y <= N:
            table[x * x * x * y] = True
    return table


def resolve():
    table = make_table()
    N = int(input())
    print(sum(table[:N + 1]))


resolve()
