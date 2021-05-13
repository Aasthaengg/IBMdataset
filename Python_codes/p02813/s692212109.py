import itertools


def abc150c_count_order():
    n = int(input())
    p = tuple(map(int, input().split()))
    q = tuple(map(int, input().split()))
    pattern = list(itertools.permutations(range(1, n + 1), n))
    print(abs(pattern.index(p)-pattern.index(q)))


abc150c_count_order()
