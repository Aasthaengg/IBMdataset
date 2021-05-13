import sys
import collections
import bisect


def main():
    n = int(input())
    under = 1
    for i in range(1, n + 1):
        under *= i

    xyList = [list(map(int, input().split())) for _ in range(n)]
    xyListSum = 0
    for xn in range(1, n):
        for yn in range(xn + 1, n + 1):
            leng = ((xyList[xn-1][0] - xyList[yn-1][0]) **
                    2 + (xyList[xn - 1][1] - xyList[yn - 1][1]) ** 2) ** 0.5
            xyListSum += leng * 2
    print(xyListSum / n)


if __name__ == '__main__':
    main()
