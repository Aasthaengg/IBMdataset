'''A - Entrance Examination
https://atcoder.jp/contests/abc117/tasks/abc117_a

>>> main(8, 3)
2.6666666667
>>> main(99, 1)
99.0000000000
>>> main(1, 100)
0.0100000000'''


def main(t, x):
    print('{:.10f}'.format(t/x))


if __name__ == "__main__":
    t, x = map(int, input().split(' '))
    main(t, x)
