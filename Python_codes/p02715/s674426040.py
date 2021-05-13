import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    D = [0] * (k + 1)

    for i in range(1, k + 1):
        D[i] = pow(k // i, n, mod)

    for i in range(k, 0, -1):
        for j in range(2 * i, k + 1, i):
            D[i] = (D[i] - D[j]) % mod

    res = 0
    for i in range(1, k + 1):
        res = (res + D[i] * i) % mod

    print(res)


if __name__ == '__main__':
    resolve()
