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
    N, *A = map(int, read().split())

    B = [False] * (N + 1)
    C = [0] * (N + 1)

    for i in range(N, 0, -1):
        if A[i-1] == C[i]:
            continue
        B[i] = True
        divs = divisors(i)
        for d in divs:
            C[d] ^= 1

    ans = [i for i in range(1, N + 1) if B[i]]
    print(len(ans))
    if len(ans) > 0:
        print(' '.join(map(str, ans)))

    return


if __name__ == '__main__':
    main()
