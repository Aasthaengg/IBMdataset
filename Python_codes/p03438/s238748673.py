import sys
input = sys.stdin.readline
from collections import Counter

def read():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    return N, A, B


def solve(N, A, B):
    # 正負の相殺操作ができる回数
    k = 0
    # 負数の合計
    m = 0
    for a, b in zip(A, B):
        d = b - a
        if d > 0:
            k += d // 2
        elif d < 0:
            m -= d
    return "Yes" if k >= m else "No"


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
