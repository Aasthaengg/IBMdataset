def count(xs, ys):
    """Returns a count of elements in xs which is also in ys.

    >>> count([1, 2, 3], [1, 3])
    2
    >>> count([1, 2, 3, 4, 5], [3, 4, 1])
    3
    """
    xset = set(xs)
    yset = set(ys)
    return len(xset & yset)


def run():
    _ = input()  # flake8: noqa
    s = [int(i) for i in input().split()]
    _ = input()  # flake8: noqa
    t = [int(j) for j in input().split()]

    print(count(s, t))


if __name__ == '__main__':
    run()

