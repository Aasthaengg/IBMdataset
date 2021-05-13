# coding:UTF-8
import sys


def resultSur97(x):
    return x % (10 ** 9 + 7)


if __name__ == '__main__':
    # ------ 入力 ------#
    # 1行入力
    s = input()    # 数字
    t = input()    # 数字

    # ------ 処理 ------#
    sMin = len(t)
    for i in range(len(s)-len(t)+1):
        str1 = s[i:i+len(t)]
        count = 0
        for j in range(len(str1)):
            if str1[j] != t[j]:
                count += 1
        if sMin > count:
            sMin = count

    # ------ 出力 ------#
    print("{}".format(sMin))
    # if flg == 0:
    #     print("YES")
    # else:
    #     print("NO")
