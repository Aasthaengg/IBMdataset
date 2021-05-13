import math


def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    n = int(input().rstrip())

    p = tuple(int(x) for x in input().rstrip().split(" "))
    q = tuple(int(x) for x in input().rstrip().split(" "))

    import itertools

    perm = itertools.permutations(list(range(1, n+1)), n)

    for i, v in enumerate(perm):
        if v == p:
            a = i
        if v == q:
            b = i

    print(abs(a-b))



if __name__ == "__main__":
    resolve()
