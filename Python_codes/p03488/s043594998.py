import sys
# gcd
# from fractions import gcd
# 切り上げ，切り捨て
# from math import ceil, floor
# リストの真のコピー（変更が伝播しない）
# from copy import deepcopy
# 累積和。list(accumulate(A))としてAの累積和
# from itertools import accumulate
# l = ['a', 'b', 'b', 'c', 'b', 'a', 'c', 'c', 'b', 'c', 'b', 'a']
# S = Counter(l)  # カウンタークラスが作られる。S=Counter({'b': 5, 'c': 4, 'a': 3})
# print(S.most_common(2))  # [('b', 5), ('c', 4)]
# print(S.keys())  # dict_keys(['a', 'b', 'c'])
# print(S.values())  # dict_values([3, 5, 4])
# print(S.items())  # dict_items([('a', 3), ('b', 5), ('c', 4)])
# from collections import Counter
# import math
# from functools import reduce
#
# input関係の定義
# fin = open('in_6.txt', 'r')
# sys.stdin = fin
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
# template

YES = "Yes"  # type: str
NO = "No"  # type: str

def iterate_tokens():
    for line in sys.stdin:
        for word in line.split():
            yield word


if __name__ == '__main__':

    tokens = iterate_tokens()
    s = list(next(tokens))  # type: str
    x = int(next(tokens))  # type: int
    y = int(next(tokens))  # type: int

    # write code
    x_axis = []
    y_axis = []
    i = 0
    cntT = 0
    cntF = 0
    for i in range(len(s)):
        if s[i] == 'T':
            if cntT % 2 == 0:
                x_axis.append(cntF)
            else:
                y_axis.append(cntF)
            cntT += 1
            cntF = 0
            continue
        else:
            cntF += 1
            continue
    if cntT % 2 == 0:
        x_axis.append(cntF)
    else:
        y_axis.append(cntF)


    x -= x_axis[0]
    del x_axis[0]
    # print(x_axis, y_axis)
    x_set = {x}
    y_set = {y}
    for num in x_axis:
        x_set = {i + k for i in x_set for k in {-num, num} if - 8000 <= i <= 8000}
    for num in y_axis:
        y_set = {i+k for i in y_set for k in {-num,num} if -8000<=i<=8000}

    # print(x_set, y_set)
    if 0 in x_set and 0 in y_set:
        print(YES)
    else:
        print(NO)

