# coding: utf-8


def solve(*args: str) -> str:
    n = int(args[0])
    return str(n//2-1 if n % 2 == 0 else n//2)


if __name__ == "__main__":
    print(solve(*(open(0).read().splitlines())))
