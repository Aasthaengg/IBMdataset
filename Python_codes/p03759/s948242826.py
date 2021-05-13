#!/usr/bin/python3
# ABC058_A
"""
ι⊥l（柱）
"""

def beautiful():
    """
    本体
    """
    a, b, c = map(int, input().split())
    if b-a == c-b:
        print('YES')
    else:
        print('NO')


def main():
    beautiful()


if __name__ == '__main__':
    main()
