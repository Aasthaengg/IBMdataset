import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
import numpy as np

def abc080_c():
    N = int(readline())  # 他店の数
    # 他店の営業パターン：店→日付→営業01
    F = np.array([list(map(int, readline().split())) for _ in range(N)], dtype=np.int32)
    # 他店と何回重なると利益がどうなるか：店→重複回数→利益
    P = np.array([list(map(int, readline().split())) for _ in range(N)], dtype=np.int32)
    ans = -10**12  # 最悪 100 * -10**7

    # bit全探索
    from itertools import product
    for mask in product(range(2), repeat=10):
        if mask.count(1) == 0: continue
        profit = 0
        for i in range(N):
            # 他店iの営業パターンと、自店の営業パターンmaskと、の要素積は、重複する営業日
            overlap = np.multiply(F[i,:], mask).sum()
            profit += P[i, overlap]
        ans = max(profit, ans)
    print(ans)

abc080_c()