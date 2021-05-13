#!/usr/bin/python3
# abc061_a
"""
Between Two Integers
"""

def main():
    """
    こたえ。
    """
    A, B, C = map(int, input().split())

    if A <= C <= B:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
