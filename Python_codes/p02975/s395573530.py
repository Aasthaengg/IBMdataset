import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    flg = False
    if len(set(A)) == 1 and 0 in set(A):
        flg = True
    else:
        if n % 3 == 0:
            D = Counter(A)
            if len(D) == 3:
                t = 0
                V = set()
                for k, v in D.items():
                    t ^= k
                    V.add(v)
                if len(V) == 1 and t == 0:
                    flg = True
            elif len(D) == 2 and D.get(0, -1) != -1:
                v = D[0]
                if n - v == n * 2 // 3:
                    flg = True
    print("Yes" if flg else "No")


if __name__ == '__main__':
    resolve()
