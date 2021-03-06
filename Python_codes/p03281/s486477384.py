import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def divisors(n):
    lower = []
    upper = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            lower.append(i)
            if i != n // i:
                upper.append(n // i)

    lower.extend(reversed(upper))
    return lower


def main():
    N = int(readline())

    ans = 0
    for n in range(1, N + 1, 2):
        if len(divisors(n)) == 8:
            ans += 1

    print(ans)
    return


if __name__ == '__main__':
    main()
