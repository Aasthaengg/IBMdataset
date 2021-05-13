import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())

    if abs(n - m) >= 2:
        print(0)
        exit()

    fact = [1]
    for i in range(2, max(n, m) + 1):
        fact.append((fact[-1] * i) % mod)

    res = fact[n - 1] * fact[m - 1] % mod
    print(res if n != m else res * 2 % mod)


if __name__ == '__main__':
    resolve()
