#!/usr/bin/env python3

import sys


def main(input):
    return input if len(input) == 2 else input[::-1]

if __name__ == "__main__":
    print(main(sys.stdin.readline().strip()))
