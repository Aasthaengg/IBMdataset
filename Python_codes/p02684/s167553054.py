# https://atcoder.jp/contests/abc167/tasks/abc167_d
# コンテスト中は周期性を用いたが、今回はdoublingで解いてみる

import sys
sys.setrecursionlimit(1 << 25)
read = sys.stdin.readline
ra = range
enu = enumerate


def exit(*argv, **kwarg):
    print(*argv, **kwarg)
    sys.exit()


def mina(*argv, sub=1): return list(map(lambda x: x - sub, argv))
# 受け渡されたすべての要素からsubだけ引く.リストを*をつけて展開しておくこと


def ints(): return list(map(int, read().split()))


MOD = 10**9 + 7
INF = 2**31  # 2147483648 > 10**9
# default import
from collections import defaultdict, Counter, deque
from operator import itemgetter, xor, add
from itertools import product, permutations, combinations
from bisect import bisect_left, bisect_right  # , insort_left, insort_right
from functools import reduce

N, K = ints()
A = mina(*ints())
# 10^18のは60bitで表せるのでnxt tableをつくるのに最大1.2 * 10^7 ぐらい。ギリ間に合いそう


nxt = [[-1] * N for _ in ra(K.bit_length())]  # [k][v]...vから2^k回移動したノード
# 初期化
for v, nx in enu(A):
    nxt[0][v] = nx

# テーブル埋め
for k in ra(K.bit_length() - 1):
    for v in ra(N):
        nxt[k + 1][v] = nxt[k][nxt[k][v]]

# 答えの取得
now = 0  # はじめは0地点にいる
for k in ra(K.bit_length()):
    if (K >> k) & 1:
        # kbit目が立ってたらこの回数分だけ移動
        now = nxt[k][now]
print(now + 1)
