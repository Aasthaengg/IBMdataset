import sys
input = sys.stdin.readline

class Doubling:
    def __init__(self, A, K_max, decrement=True):
        """
        :param A: リスト。i から A[i] へと移動する
        :param K_max: K_max = 2**(k_max) まで参照する可能性がある
        :param decrement: True = A の要素の decrement が必要
        """
        self.k_max = K_max.bit_length()
        self.n = len(A)
        self.decrement = decrement
        self.doubling = [[-1] * self.n for _ in range(self.k_max)]
        for i, a in enumerate(A):
            self.doubling[0][i] = a - self.decrement

        for i in range(1, self.k_max):
            for j in range(self.n):
                if self.doubling[i - 1][j] != -1:
                    self.doubling[i][j] = self.doubling[i - 1][self.doubling[i - 1][j]]

    def apply(self, start, K):
        """
        :param start: スタート地点
        :param K: K回進む
        :return:
        """
        i = start - self.decrement
        for k in range(K.bit_length()):
            m = 1 << k
            if m & K:
                i = self.doubling[k][i]
            if i is None:
                break
        return i + self.decrement


######################################################################################


N, K = map(int, input().split())
A = list(map(int, input().split()))
doubling = Doubling(A, 10**18 + 1, decrement=True)
print(doubling.apply(1, K))