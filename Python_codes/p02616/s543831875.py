import sys
input = sys.stdin.readline
from itertools import accumulate
from functools import reduce
from operator import mul
from bisect import bisect_left


def read():
    N, K = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    return N, K, A


def sign(x):
    if x == 0:
        return 0
    return 1 if x > 0 else -1


def solve(N, K, A, p=10**9+7):
    A.sort(key=lambda a: -abs(a))
    s = 1  # sign
    v = 1  # value
    idx_minus = -1
    idx_not_minus = -1
    for i in range(K):
        _s = sign(A[i])
        s *= _s
        v *= A[i]
        v %= p
        if _s >= 0:
            idx_not_minus = i
        else:
            idx_minus = i
    if s >= 0 or N == K:
        return v
    
    # 以下、左からK個を掛けた数が負になるとき
    # 絶対値が小さな負の数を1つ取り除いて、絶対値が大きな正の数を1つ追加する
    a1 = A[idx_minus]
    b1 = max(A[K:])
    # 絶対値が小さな正の数を1つ取り除いて、絶対値が大きな負の数を1つ追加する
    a2 = A[idx_not_minus]
    b2 = min(A[K:])

    use_1, use_2 = True, True
    if not(idx_minus >= 0 and b1 >= 0):
        use_1 = False
    if not(idx_not_minus >= 0 and b2 < 0):
        use_2 = False
    
    if use_1 and use_2:
        if b1 * a2 >= b2 * a1:
            use_1 = True
            use_2 = False
        else:
            use_1 = False
            use_2 = True
    if use_1:
        v *= pow(a1, p-2, p)
        v %= p
        v *= b1
        v %= p
    elif use_2:
        v *= pow(a2, p-2, p)
        v %= p
        v *= b2
        v %= p
    else:
        # どうやっても正の数が作れないとき
        A.sort(key=lambda a: abs(a))
        s = 1
        v = 1
        for i in range(K):
            _s = sign(A[i])
            s *= _s
            v *= A[i]
            v %= p
    return v


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
