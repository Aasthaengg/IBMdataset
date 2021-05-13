# coding: utf-8


def solve(*args: str) -> str:
    x, y = map(int, args[0].split())

    count = 0
    while x <= y:
        count += 1
        x *= 2

    return str(count)


if __name__ == "__main__":
    print(solve(*(open(0).read().splitlines())))
