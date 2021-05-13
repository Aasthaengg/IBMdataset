# coding: utf-8


def solve(*args: str) -> str:
    N = list(map(int, args[0]))

    a, b = 0, 1
    for n in N:
        a, b = min(b+(10-n), a+n), min(b+(9-n), a+n+1)
    return str(a)


if __name__ == "__main__":
    print(solve(*(open(0).read().splitlines())))
