#!/usr/bin/env python3
import re


def main():
    S = input()
    if re.match(r'^(?:hi)+$', S):
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
