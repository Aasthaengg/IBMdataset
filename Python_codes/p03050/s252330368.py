import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def main():
    N = int(readline())
    div = divisors(N)
    ans = 0
    for m in div:
        if m!=1:
            if N//(m-1) == N%(m-1):
                ans += m-1
    print(ans)


if __name__ == '__main__':
    main()
