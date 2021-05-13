# https://atcoder.jp/contests/abc098/tasks/arc098_b
import sys
read = sys.stdin.readline


def read_ints():
    return list(map(int, read().split()))


class CumSum1d:
    def __init__(self, ls: list):
        '''
        1次元リストを受け取る
        '''
        from itertools import accumulate
        self.ls_accum = [0] + list(accumulate(ls))

    def total(self, i, j):
        # もとの配列lsにおける[i,j)の中合計
        return self.ls_accum[j] - self.ls_accum[i]


class CumXor1d:
    def __init__(self, ls: list):
        '''
        1次元リストを受け取る
        '''
        self.ls_accum = [0]
        for l in ls:
            self.ls_accum.append(l ^ self.ls_accum[-1])

    def total(self, i, j):
        # もとの配列lsにおける[i,j)の中合計
        return self.ls_accum[j] ^ self.ls_accum[i]


from collections import deque
N = int(input())
A = read_ints()

# どの[ii,jj)を持ってきてもxorsumとaddsumが成り立つ最長の区間[i,j)に対してn=j-iに対してn * (n - 1) // 2 + n をすれば良い ? いや若干ダブりが存在して微妙に合わない
# 一旦最長の区間のidxを取得してダブリの区間はその後に考慮しよう?
# 前処理としてxorとadd両方の累積xorと累積和を作ってあげる
# でi,jを尺取法などで取得すれば良い

cumsum = CumSum1d(A)
cumxor = CumXor1d(A)
# 尺取法でaddとxorした区間和が一致する一番長い[i,j)を取ってくる
ids = []
r_pre = 0
for l in range(0, N):
    r = max(r_pre, l + 1)  # ありえるidxに
    while r <= N and cumsum.total(l, r) == cumxor.total(l, r):
        r += 1  # totalのrはすでに半開区間 それを満たさなくなったときのrとしたら半開区間の更にその先に行く
    r -= 1  # 行き過ぎた分を調整
    if r != r_pre:
        r_pre = r
        ids.append((l, r))


ans = 0
for l, r in ids:
    n = r - l
    ans += n + n * (n - 1) // 2
# さらにダブっている部分を取り除く
if len(ids) > 1:
    for (_, r), (l, _) in zip(ids, ids[1:]):
        n = max(0, r - l)
        ans -= n + n * (n - 1) // 2


print(ans)
