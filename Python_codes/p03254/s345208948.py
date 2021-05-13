#!/usr/bin/env python3


def main():
    N, x, *A = map(int, open(0).read().split())
    A.sort()
    for i in range(N):
        x -= A[i]
        if x == 0:
            print(i + 1)
            break
        elif x < 0:
            print(i)
            break
    else:
        # ちょうどN個もらわないと喜べない悲しい子どもたち
        print(N - 1)


main()
