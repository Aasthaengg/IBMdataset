import numpy as np
from numba import njit


def main(N, K, A):
    @njit(cache = True) # numpyの高速化．雲泥の差になった．知らなかった．
    def rep(N, A):
        B = np.zeros(N + 1, dtype=np.int64) # np.int64としないとnjitがエラー
        for x in range(N):
            minimum = max(0, x - A[x])
            maximum = min(N, x + A[x] + 1)
            # B[minimum:maximum] += 1   # これだと実質for文回してるような感じだから遅い？
            B[minimum] += 1
            B[maximum] -= 1
        # return B  # これだと実質for文回してるような感じだから遅い？
        return np.cumsum(B)[:-1]

    A = np.array(A, dtype=np.int64)
    for k in range(K):
        B = rep(N, A)
        if np.array_equal(A, B):
            break
        else:
            A = B
    return A



if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    print(' '.join([str(i) for i in main(N, K, A)]))