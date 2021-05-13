def ri():
    return int(input())


def rii():
    return [int(v) for v in input().split()]


def solve(*args):
    a, b, c, d = args
    return max(a * c, a * d, b * c, b * d)


if __name__ == "__main__":
    print(solve(*rii()))