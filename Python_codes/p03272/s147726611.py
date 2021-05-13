#!/usr/bin/env python3

def main():
    na = list(map(int, input().split()))
    N, i = na[0], na[1]

    print(N + 1 - i)


if __name__ == '__main__':
    main()

