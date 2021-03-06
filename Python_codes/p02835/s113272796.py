#!/usr/bin/env python3


def solve(A: "List[int]"):
    return ["win", "bust"][sum(A) >= 22]


def main():
    A = list(map(int, input().split()))
    answer = solve(A)
    print(answer)


if __name__ == "__main__":
    main()
