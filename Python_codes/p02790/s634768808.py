#!/usr/bin/env python3


def solve(a: int, b: int):
    n1 = str(a) * b
    n2 = str(b) * a
    if n1 < n2:
        return n1
    else:
        return n2


def main():
    a, b = map(int, input().split())
    answer = solve(a, b)
    print(answer)


if __name__ == "__main__":
    main()
