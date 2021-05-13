import itertools


def actual(n, D):
    comb = itertools.combinations(D, 2)

    return sum([x * y for x, y in comb])

n = int(input())
D = map(int, input().split())

print(actual(n, D))