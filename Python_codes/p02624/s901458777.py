import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    L = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            L[j] += 1
    res = 0
    for i in range(1, n + 1):
        res += i * L[i]
    print(res)


if __name__ == '__main__':
    resolve()
