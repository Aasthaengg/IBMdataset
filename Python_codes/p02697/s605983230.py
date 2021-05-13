def e_rotation_matching():
    # 参考: https://maspypy.com/atcoder-参加感想-2020-05-02abc-165
    import numpy as np
    N, M = [int(i) for i in input().split()]

    A = np.arange(M)  # 剰余計算の簡便のため、0-origin とする
    B = 2 * M - 1 - A  # N >= 2*M - 1 だが、N = 2*M - 1 の場合と同じ構築でよい
    # 剰余を取ったときに mod N に対して A, B の全要素が互いに異なるようにしたい
    B[:M // 2] -= (2 * M + 1)

    A %= N  # 全要素は正整数でないといけない
    B %= N
    A += 1  # A, B は 0-origin としていたため
    B += 1
    return '\n'.join([f'{a} {b}' for a, b in zip(A.tolist(), B.tolist())])

print(e_rotation_matching())