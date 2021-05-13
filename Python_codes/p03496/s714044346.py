import sys
from collections import defaultdict
from heapq import *
def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    A = list(map(int, input().split()))
    """
    すべて正の場合は簡単で、
        ai > a(i+1) <= a(i+2) <= ... <= aj > a(j+1) <= ...
    となっていたらa(i+1)~ajすべてにaiを加えればよい。

    実はすべて負の場合も同様で、上のようになっていたら
    ai~ajすべてにa(j+1)を加えればよい。

    「「部分問題が解けたのだから、一般の場合はここに帰着させる！！！」」
    すなわち正負が混ざっている場合は、Aの最大値もしくは最小値をすべての要素に
    足すことで、すべて正もしくはすべて負にすることができるので解けた。
    """
    M_idx, m_idx = 0, 0
    M, m = A[0], A[0]
    for i, a in enumerate(A):
        if a > M:
            M_idx, M = i, a
        if a < m:
            m_idx, m = i, a
    print(2 * n - 1)
    if M >= -m:
        for i in range(n): print(M_idx + 1, i + 1)
        for i in range(n - 1): print(i + 1, i + 2)
    else:
        for i in range(n): print(m_idx + 1, i + 1)
        for i in range(n, 1, -1): print(i, i - 1)
    



if __name__ == "__main__":
    main()
