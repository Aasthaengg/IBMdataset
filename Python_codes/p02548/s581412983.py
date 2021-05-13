# coding:UTF-8
import sys
from math import factorial, ceil, floor

MOD = 10 ** 9 + 7
INF = 10000000000


def main():
    # ------ 入力 ------#
    n = int(input())    # 数字

    # ------ 処理 ------#
    result = 0
    for a in range(1, n+1):
        tmp = (n - 1) // a
        result += tmp

    # ------ 出力 ------#
    print("{}".format(result))

if __name__ == '__main__':
    main()
