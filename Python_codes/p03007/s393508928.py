import sys
import copy
from collections import deque

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    if A[0] >= 0:
        ans = sum(A[1:]) - A[0]
        plus = copy.deepcopy(A[1:])
        minus = [A[0]]
    elif A[-1] <= 0:
        ans = -sum(A[:-1]) + A[-1]
        plus = [A[-1]]
        minus = copy.deepcopy(A[:-1])
    else:
        plus = []
        minus = []
        ans = 0
        for a in A:
            if a >= 0:
                ans += a
                plus.append(a)
            else:
                ans -= a
                minus.append(a)

    plus = deque(plus)
    minus = deque(minus)
    print(ans)

    # minusをまず一つにする
    while len(minus) > 1:
        p = plus.pop()
        m = minus.pop()
        print(p, m)
        plus.append(p - m)

    # minusが1つになったあとの処理
    p = plus.pop()
    m = minus.pop()
    if len(plus) == 0:
        print(p, m)
        return

    print(m, p)
    cur = m - p
    while len(plus) > 1:
        p = plus.pop()
        print(cur, p)
        cur -= p
    if len(plus) != 0:
        p = plus.pop()
        print(p, cur)


if __name__ == "__main__":
    main()
