import sys

input = sys.stdin.readline
P = 10 ** 9 + 7


def main():
    N, K = map(int, input().split())

    ans = 0
    n_gcd = dict.fromkeys(range(K + 1), 0)
    for k in reversed(range(1, K + 1)):
        n_gcd[k] = pow(K // k, N, mod=P)
        for m in range(2, K // k + 1):
            n_gcd[k] = (n_gcd[k] - n_gcd[k * m]) % P
        ans = (ans + k * n_gcd[k]) % P

    print(ans)


if __name__ == "__main__":
    main()
