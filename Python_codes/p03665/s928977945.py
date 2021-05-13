import math


# 組み合わせの計算
def C(n, r):
    ret = math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
    return ret


# 組み合わせの総和こ計算
# nCr + nCr-1 + ... + nC0
def sum_C(n, R):
    nCr_0 = 1

    s = nCr_0
    for r in range(min(n, R)):
        nCr_1 = nCr_0 * (n - r) // (r + 1)
        nCr_0 = nCr_1
        s += nCr_1

    return s


# nC0, nC1, nC2, ..., nCrの答えをlistで返す
def list_conb(n, R):
    nCr_0 = 1

    ret = [nCr_0]
    for r in range(min(n, R)):
        nCr_1 = nCr_0 * (n - r) // (r + 1)
        ret.append(nCr_1)
        nCr_0 = nCr_1

    return ret


def main():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))

    A = [a % 2 for a in A]

    n_1 = sum(A)
    n_0 = N - n_1

    # 0 -> 1の数が偶数
    # 1 -> 1の数が奇数

    c = 0
    # 1の袋をi個選び0の袋を好きな個数選ぶ
    if P == 0:
        r = range(0, n_1 + 1, 2)
    else:
        r = range(1, n_1 + 1, 2)

    for i in r:  # 偶数
        if N - i < 0:
            break
        c += C(n_1, i) * sum_C(n_0, N - i)

    print(c)


main()
