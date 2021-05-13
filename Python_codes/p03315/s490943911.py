import numpy as np
import sys
input = sys.stdin.readline


def main():
    s = input()
    plus = s.count("+")
    minus = s.count("-")
    print(plus - minus)


if __name__ == "__main__":
    main()