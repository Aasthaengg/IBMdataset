import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def enum_primes(n):
    flag_num = (n + 1) // 2
    prime_flag = [True] * flag_num

    for num in range(3, int(n ** 0.5) + 1, 2):
        idx = (num - 1) // 2 - 1
        if prime_flag[idx]:
            for j in range(idx + num, flag_num, num):
                prime_flag[j] = False

    primes = [2]
    temp = [(i+1) * 2 + 1 for i in range(flag_num) if prime_flag[i]]
    primes.extend(temp)

    return primes


def main():
    n = int(readline())
    primes = set(enum_primes(55555))
    x = []
    l = 0
    for prime in primes:
        if len(x) == n:
            break
        if prime % 5 == 1:
            x.append(prime)
    print(*x)


if __name__ == '__main__':
    main()
