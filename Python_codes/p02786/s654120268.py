#!/usr/bin/env python3


def solve(H: int):
    n = 1
    attack = 0
    while H > 1:
        attack += n
        H = H // 2
        n *= 2
    attack += n
    return attack


def main():
    H = int(input())
    answer = solve(H)
    print(answer)


if __name__ == "__main__":
    main()
