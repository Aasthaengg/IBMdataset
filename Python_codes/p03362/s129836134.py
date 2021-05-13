import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())
    n = 55555
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False

    primes = []
    for i in range(2, n):
        if is_prime[i]:
            primes.append(i)

    ans = [2]
    cnt = 1
    for p in primes[1:]:
        a = p // 2
        if a % 5 == 1:
            ans.append(p)
            cnt += 1

            if cnt == N:
                break

    print(*ans, sep=" ")


if __name__ == "__main__":
    main()
