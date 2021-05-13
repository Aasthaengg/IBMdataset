#!/usr/bin/env python3

ABC = "ABC"
ARC = "ARC"


def solve(S: str):
    if S == ABC:
        return ARC
    else:
        return ABC


def main():
    S = input().strip()
    answer = solve(S)
    print(answer)


if __name__ == "__main__":
    main()
