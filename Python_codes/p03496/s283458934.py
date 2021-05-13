import sys
# gcd
# from bisect import bisect_left,bisect_right
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
# fin = open('in_1.txt', 'r')
# sys.stdin = fin
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
# template


def iterate_tokens():
    for line in sys.stdin:
        for word in line.split():
            yield word


if __name__ == '__main__':

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"

    # write code
    anslist = []
    MAX_A = max(a)
    MIN_A = min(a)
    if MIN_A >= 0:
        for i in range(1, N):
            anslist.append((i,i+1))
    elif MAX_A < 0:
        for i in range(N, 1, -1):
            anslist.append((i, i - 1))
    else:
        if abs(MAX_A) >= abs(MIN_A):
            MAX_INDEX = a.index(MAX_A)
            for i in range(1,N+1):
                anslist.append((MAX_INDEX+1, i))
            for i in range(1, N):
                anslist.append((i, i + 1))
        else:
            MIN_INDEX = a.index(MIN_A)
            for i in range(1, N + 1):
                anslist.append((MIN_INDEX+1, i))
            for i in range(N, 1, -1):
                anslist.append((i, i - 1))

            
    print(len(anslist))
    for tup in anslist:
        print(tup[0],tup[1])
