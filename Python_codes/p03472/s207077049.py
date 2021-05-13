import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 998244353


def resolve():
    n, h = map(int, input().split())
    A, B = [], []
    for _ in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    MAX_A = max(A)
    B.sort(reverse=True)
    que = deque(B)

    res = 0
    while h > 0:
        if que and MAX_A < que[0]:
            damage = que.popleft()
            h -= damage
            res += 1
        else:
            res += (h + MAX_A - 1) // MAX_A
            h = 0

    print(res)


if __name__ == '__main__':
    resolve()
