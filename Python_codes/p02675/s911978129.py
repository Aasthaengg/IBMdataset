#!/usr/bin/env python3


def solve(N: str):
    return {
        "0": "pon",
        "1": "pon",
        "2": "hon",
        "3": "bon",
        "4": "hon",
        "5": "hon",
        "6": "pon",
        "7": "hon",
        "8": "pon",
        "9": "hon",
    }[N[-1]]


def main():
    S = input()
    answer = solve(S)
    print(answer)


if __name__ == "__main__":
    main()
