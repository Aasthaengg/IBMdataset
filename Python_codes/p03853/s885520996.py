#!/usr/bin/env python3

from typing import List


def main():
    args = input().split()
    H = int(args[0])
    W = int(args[1])

    result: List[str] = []
    for row in range(H):
        rowStr = input()
        result.append(rowStr)
        result.append(rowStr)

    for item in result:
        print(item)


if __name__ == "__main__":
    main()
