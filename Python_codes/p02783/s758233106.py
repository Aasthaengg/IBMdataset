#!/usr/bin/env python3


def solve(H: int, A: int):
    return (H + A - 1) // A


def main():
    H, A = map(int, input().split())
    answer = solve(H, A)
    print(answer)


if __name__ == "__main__":
    main()
