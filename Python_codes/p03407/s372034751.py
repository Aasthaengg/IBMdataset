#!/usr/bin/env python3

def main():
    na = list(map(int, input().split()))
    A, B, C = na[0], na[1], na[2]

    print('Yes' if C <= A + B else 'No')


if __name__ == '__main__':
    main()

