import sys
sys.setrecursionlimit(1 << 25)
read = sys.stdin.readline
ra = range
enu = enumerate


def read_ints():
    return list(map(int, read().split()))


def read_a_int():
    return int(read())


def read_tuple(H):
    '''
    H is number of rows
    '''
    ret = []
    for _ in range(H):
        ret.append(tuple(map(int, read().split())))
    return ret


def read_col(H):
    '''
    H is number of rows
    A列、B列が与えられるようなとき
    ex1)A,B=read_col(H)    ex2) A,=read_col(H) #一列の場合
    '''
    ret = []
    for _ in range(H):
        ret.append(list(map(int, read().split())))
    return tuple(map(list, zip(*ret)))


def read_matrix(H):
    '''
    H is number of rows
    '''
    ret = []
    for _ in range(H):
        ret.append(list(map(int, read().split())))
    return ret
    # return [list(map(int, read().split())) for _ in range(H)] # 内包表記はpypyでは遅いため


MOD = 10**9 + 7
INF = 2**31  # 2147483648 > 10**9
# default import
from collections import defaultdict, Counter, deque
from operator import itemgetter
from itertools import product, permutations, combinations
from bisect import bisect_left, bisect_right  # , insort_left, insort_right

# https://atcoder.jp/contests/abc121/tasks/abc121_d

# xorとは繰り上がりのない足し算である

# f(A,B)=f(0,B)-f(0,A-1)
# f(0,i)をどうやって高速に求めるか？
# 各桁独立、ibit目に登場した1の数の偶奇でわかる
# しかも4つごとに周期が存在する(4*n -1 のときはかならず0になるのでこれを利用できる)


def f(x):
    start = x // 4 * 4
    ret = 0
    for i in ra(start, x + 1):
        ret ^= i
    return ret


A, B = read_ints()
# print(f(B), f(A - 1))
print(f(B) ^ f(A - 1))
