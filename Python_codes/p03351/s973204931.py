'''A - Colorful Transceivers
https://atcoder.jp/contests/abc097/tasks/abc097_a

>>> main(4, 7, 9 ,3)
Yes
>>> main(100, 10, 1 ,2)
No
>>> main(10, 10, 10 ,1)
Yes
>>> main(1, 100, 2, 10)
Yes
'''


def main(a, b, c, d):
    if abs(a-c) <= d or abs(a-b) <= d and abs(b-c) <= d:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    a, b, c, d = map(int, input().split(' '))

    main(a, b, c, d)
