
import math


def solve(R: int):
    return 2 * math.pi * R


def main():
    R = int(input())
    answer = solve(R)
    print(answer)


if __name__ == "__main__":
    main()
