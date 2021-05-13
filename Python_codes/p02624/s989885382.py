import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    prime_cnt = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(0, n + 1, i):
            prime_cnt[j] += 1

    res = 0
    for i in range(1, n + 1):
        res += i * prime_cnt[i]
    print(res)


if __name__ == '__main__':
    resolve()
