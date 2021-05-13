import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


# nが素数か判定する
def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(pow(n, 0.5)) + 1):
        if n % k == 0:
            return False
    return True


def resolve():
    n = int(input())
    primes = []
    for i in range(1, 55556):
        if i % 5 == 1 and is_prime(i):
            primes.append(i)
            if len(primes) == n:
                break
    print(*primes)


if __name__ == '__main__':
    resolve()
