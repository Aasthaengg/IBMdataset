#!/usr/bin/env python3
def main():
    A, B = map(int, input().split())

    print('IMPOSSIBLE') if (A + B) % 2 else print((A + B) // 2)


if __name__ == '__main__':
    main()
