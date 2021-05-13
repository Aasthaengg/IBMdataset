import random
import sys

import numpy as np

global NN
NN = 26

readline = sys.stdin.buffer.readline


class Contest:
    """
    d: ある日付
    i: テストの種類
    self.day: 最後にテストiを開催した日
    """

    def __init__(self, c, s, D):
        self.last = [-1 for _ in range(NN)]
        self.C = c
        self.S = s
        self.score = 0

    def minus_score(self, d, i):
        m = self.C[i] * (d - self.last[i])
        return m

    def sum_minus_scores(self, d):
        m = 0
        for i in range(NN):
            m += self.minus_score(d, i)

        return m

    # テストiを開催したときのスコア
    def update_score(self, i, d):
        self.last[i] = d
        self.score += S[d][i]
        self.score -= self.sum_minus_scores(d)
        return self.score

    # 日付を更新せずにスコアを計算
    def calc_score(self, i, d):
        s = self.score
        last_d = self.last[i]
        self.last = d
        s += S[d][i]
        s -= self.sum_minus_scores(d)
        self.last = last_d

        return s


D = int(input())
C = list(map(int, input().split()))
S = [list(map(int, input().split())) for _ in range(D)]

tests = [int(input()) for _ in range(D)]

tests = [i - 1 for i in tests]

T = Contest(C, S, D)

for d, test in enumerate(tests):
    print(T.update_score(test, d))

