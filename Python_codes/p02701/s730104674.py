#!/usr/bin/env python3
def main():
    N = int(input())

    S = []
    for _ in range(N):
        S.append(input())
    S = set(S)
    print(len(S))


if __name__ == '__main__':
    main()
