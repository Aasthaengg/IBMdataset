'''A - Train
https://atcoder.jp/contests/abc107/tasks/abc107_a

>>> main(4, 2)
3
>>> main(1, 1)
1
>>> main(15, 11)
5'''


def main(n, i):
    print(n - i + 1)


if __name__ == '__main__':
    n, i = map(int, input().split(' '))
    main(n, i)
