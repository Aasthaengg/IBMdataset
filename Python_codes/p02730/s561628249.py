#!/usr/bin/env python3
def main():
    S = input()

    N = len(S)
    if S[:(N - 1) // 2] == S[(N + 3) // 2 - 1:]:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
