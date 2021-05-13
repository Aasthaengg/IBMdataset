import sys
import collections

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    H, W = [int(x) for x in input().split()]
    A = [input().strip() for _ in range(H)]

    c = collections.Counter()
    for a in A:
        for aa in a:
            c[aa] += 1

    four_cnt = (H // 2) * (W // 2)
    two_cnt = (H % 2) * (W // 2) + (W % 2) * (H // 2)
    one_cnt = (H % 2) * (W % 2)

    for k in c.keys():
        if c[k] >= 4:
            q, r = divmod(c[k], 4)
            mi = min(four_cnt, q)
            c[k] -= mi * 4
            four_cnt -= mi

    for k in c.keys():
        if c[k] >= 2:
            q, r = divmod(c[k], 2)
            mi = min(two_cnt, q)
            c[k] -= mi * 2
            two_cnt -= mi

    for k in c.keys():
        if c[k] >= 1:
            q, r = divmod(c[k], 1)
            mi = min(one_cnt, q)
            c[k] -= mi * 1
            one_cnt -= mi

    if sum([four_cnt, two_cnt, one_cnt]) == 0:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
