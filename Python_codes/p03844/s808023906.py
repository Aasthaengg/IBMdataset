print(eval(input()))
"""
import os
import sys
import random
import numpy as np
import scipy.stats as stats
import matplotlib as mpl;mpl.use('TkAgg')
import matplotlib.pyplot as plt

mpl.rcParams['axes.xmargin'] = 0
mpl.rcParams['axes.ymargin'] = 0
plt.rcParams['figure.figsize'] = (14, 7)


class Bingo:
    # 各変数の初期化
    def __init__(self):
        self.li = []  # ビンゴカードに配置する数字
        self.bingo = [[0 for i in range(5)] for j in range(5)]  # ビンゴカード(5*5の2次元配列)
        self.bingo_state = [[0 for i in range(5)] for j in range(5)]  # ビンゴカードの状態(5*5の2次元配列)
        self.lot = []  # 抽選された数字を保持
        self.num = list(range(1, 76, 1))  # 1-75の数字が入ったリスト
        self.counter = 0  # 穴の開いた個数をカウント
        self.latest_i = 0  # 最新の穴のy座標
        self.latest_j = 0  # 最新の穴のx座標
        self.flag = 0  # ビンゴのやつ

    # ビンゴカードに配置する数字を決定
    def __decision(self):
        while len(self.li) < 25:  # 数字が25個になるまで
            rnd = random.randint(1, 75)  # 1～75の乱数を生成
            if self.li.count(rnd) == 0:  # 生成された乱数がlistに存在しなければ追加
                self.li.append(rnd)
            if len([j for j in self.li if j <= 15 and not j <= 0]) > 5 \
                    or len([j for j in self.li if j <= 30 and not j <= 15]) > 5 \
                    or len([j for j in self.li if j <= 45 and not j <= 30]) > 5 \
                    or len([j for j in self.li if j <= 60 and not j <= 45]) > 5 \
                    or len([j for j in self.li if j <= 75 and not j <= 60]) > 5:
                self.li.remove(rnd)
        self.li.sort()

    # ビンゴカード(2次元配列)に数字を配置
    def set(self):
        self.__decision()
        index = 0
        for i in range(5):
            for j in range(5):
                if i == 2 and j == 2:
                    self.bingo[j][i] = 'free'
                    index += 1
                else:
                    self.bingo[j][i] = str(self.li[index])
                    index += 1
        self.bingo_state[2][2] = 1
        self.li.pop(12)

    # 抽選
    def __lottery(self):
        rnd = self.num[random.randint(0, len(self.num) - 1)]
        self.num.remove(rnd)
        self.lot.append(rnd)

    # 判定
    def __judge(self):
        # 抽選数字の有無の判定
        self.__lottery()
        number = self.lot[-1]
        if self.li.count(number) == 1:
            for i in range(5):
                for j in range(5):
                    if self.bingo[i][j] == str(number):
                        self.bingo_state[i][j] = 1
                        self.counter += 1
                        self.latest_i = i
                        self.latest_j = j
                        break
                else:
                    continue
                break
            if self.counter >= 4:
                # ビンゴの有無の判定

                # 縦
                for i in range(5):
                    if self.bingo_state[i][self.latest_j] == 0:
                        break
                    elif i == 4:
                        self.flag = 1

                # 横
                if self.flag == 0:
                    for j in range(5):
                        if self.bingo_state[self.latest_i][j] == 0:
                            break
                        elif j == 4:
                            self.flag = 1

                # 斜め
                if self.flag == 0:
                    if self.latest_i == self.latest_j:
                        for i in range(5):
                            if self.bingo_state[i][i] == 0:
                                break
                            elif i == 4:
                                self.flag = 1
                    elif self.latest_i + self.latest_j == 4:
                        ii = 0
                        jj = 4
                        for _ in range(5):
                            if self.bingo_state[ii][jj] == 0:
                                break
                            elif ii == 4 and jj == 0:
                                self.flag = 1
                            ii += 1
                            jj -= 1

    # ビンゴにかかった回数を返すよ
    def get(self):
        while self.flag == 0:
            self.__judge()
        return len(self.lot)


def display(result):
    print('total=' + str(len(result)))
    print('max=' + str(np.max(result)))
    print('min=' + str(np.min(result)))
    print('average=' + str(np.mean(result)))
    print('median=' + str(np.median(result)))
    print('mode=' + str(stats.mode(result)))


def make_fig(result):
    fig = plt.figure()
    plt.title('BINGO', fontsize=20)
    plt.grid(True)
    plt.xticks(list(range(1, 75, 2)))
    plt.hist(result, bins=75, range=(1, 75), alpha=0.8, color='c')
    # plt.show()
    fig.savefig('hist.png')


def main():
    args = sys.argv  # コマンドライン引数
    times = int(args[1])
    result = np.empty(0)

    for a in range(1, times + 1):
        if times >= 100:
            if a % int(times / 100) == 0:
                print(str(int(a * 100 / times)) + '%')
        bingo = Bingo()
        bingo.set()
        result = np.append(result, bingo.get())

    result.sort()
    make_fig(result)
    display(result)


if __name__ == '__main__':
    main()
"""