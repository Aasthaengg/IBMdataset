import math
import sys
import collections
import bisect


def main():
    h, w = map(int, input().split())
    hw = [["."] * (w + 2)] + [0] * h + [["."] * (w + 2)]
    for i in range(h):
        hw[i + 1] = ["."] + list(input()) + ["."]
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if hw[i][j] == "#":
                if hw[i - 1][j] == "#" or hw[i + 1][j] == "#" or hw[i][j - 1] == "#" or hw[i][j + 1] == "#":
                    continue
                else:
                    print("No")
                    return
    print("Yes")


if __name__ == '__main__':
    main()
