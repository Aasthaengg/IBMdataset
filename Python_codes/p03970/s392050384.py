'''A - Signboard
https://atcoder.jp/contests/code-festival-2016-qualb/tasks/codefestival_2016_qualB_a

>>> main('C0DEFESTIVAL2O16')
2
>>> main('FESTIVAL2016CODE')
16
'''


def main(s):
    base = 'CODEFESTIVAL2016'
    count = 0

    for _s, _b in zip(s, base):
        if _s != _b:
            count += 1

    print(count)


if __name__ == "__main__":
    main(input())
