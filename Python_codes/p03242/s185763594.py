#!/usr/bin/env python3


def main():
    N = input()

    ans = ''
    for n in N:
        if n == '1':
            ans += '9'
        else:
            ans += '1'
    print(ans)


if __name__ == "__main__":
    main()
