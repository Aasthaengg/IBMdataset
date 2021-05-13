'''A - B +/- A
https://atcoder.jp/contests/abc118/tasks/abc118_a

>>> main(4, 12)
16
>>> main(8, 20)
12
>>> main(1, 1)
2
'''


def main(a: int, b: int):
    if (b % a) == 0:
        print(a+b)
    else:
        print(b-a)


if __name__ == "__main__":
    a, b = map(int, input().split(' '))
    main(a, b)
