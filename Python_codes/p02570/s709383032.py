# coding:UTF-8
import sys


def resultSur97(x):
    return x % (10 ** 9 + 7)


if __name__ == '__main__':
    # ------ 入力 ------#
    aList = list(map(int, input().split()))     # スペース区切り連続数字


    # ------ 出力 ------#
    if aList[0] <= aList[1] * aList[2]:
        print("Yes")
    else:
        print("No")
