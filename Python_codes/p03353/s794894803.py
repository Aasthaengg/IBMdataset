#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    S = input()
    K = int(input())
    result = set()

    for i in range(5):
        for j in range(len(S)):
            result.add(S[j:j + i + 1])

    print(sorted(result)[K - 1])


if __name__ == "__main__":
    main()
