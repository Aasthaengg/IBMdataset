N, T = map(int, input().split())
a = list(map(int, input().split()))

# 準備
N0 = 2 ** (N - 1).bit_length()
data = [float('inf')] * (2 * N0)

# a_k の値を x に更新
def update(k, x):
    k += N0 - 1
    data[k] = x
    while k >= 0:
        k = (k - 1) // 2
        data[k] = min(data[2 * k + 1], data[2 * k + 2])

# [a_l, a_(l+1), ..., a_(r-1)]の最小値を求める
def query(l, r):
    L = l + N0
    R = r + N0
    s = float('inf')
    while L < R:
        if R & 1:
            R -= 1
            s = min(s, data[R - 1])

        if L & 1:
            s = min(s, data[L - 1])
            L += 1
        L >>= 1
        R >>= 1
    return s


# まずupdate()を使ってa_kの値を更新
for i in range(len(a)):
    update(i, -a[i])

from collections import defaultdict
dic = defaultdict(int)
for L in range(1, N):
    d = -a[L - 1] - query(L, N)
    if d > 0:
        dic[d] += 1

print(dic[sorted(dic.keys())[-1]])
