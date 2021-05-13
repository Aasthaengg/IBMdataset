'''
A - Rated for Me
https://atcoder.jp/contests/abc104/tasks/abc104_a

>>> main(1199)
ABC
>>> main(1200)
ARC
>>> main(4208)
AGC
'''


def main(r):
    if r < 1200:
        print('ABC')
    elif r < 2800:
        print('ARC')
    else:
        print('AGC')


if __name__ == "__main__":
    r = int(input())
    main(r)
