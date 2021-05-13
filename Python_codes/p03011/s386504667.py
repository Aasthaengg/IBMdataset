import itertools


def resolve():
    P, Q, R = map(int, input().split())
    groups = itertools.combinations([P, Q, R], 2)

    ans = sum([P, Q, R])
    for group in groups:
        ans = min(sum(group), ans)

    print(ans)


resolve()