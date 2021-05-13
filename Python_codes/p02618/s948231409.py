import time


def data_input():
    D = int(input())
    C = tuple(map(int, input().split()))

    S = [list(map(int, input().split())) for _ in range(D)]

    return D, C, S


def score(D, C, S, T):
    """入力D, C, Sと出力Tからスコアを計算する関数"""

    last = [0] * 26  # 0で初期化されている

    def decrease(d):
        """d日めにiを開催した時の満足度の減少を返す関数"""
        res = 0
        base = sum(C)
        for i in range(26):
            res += S[d][i] - C[i] * (d+1 - last[i])
        return res

    v = 0
    for d, i in enumerate(T):
        last[i] = d + 1
        v += decrease(d)
    return v


start_time = time.time()
D, C, S = data_input()
input_time = time.time() - start_time

T = []
# Cum_v = []
max_v = 0
for d in range(D):
    max_t = 0
    for i in range(26):
        v = score(d, C, S[:d+1], T+[i])
        if v > max_v:
            # print(f'local_max at {d}-day is updated to {v}')
            max_t = i
            max_v = v
    T.append(max_t)
    print(max_t+1)