import sys

input = sys.stdin.readline


def main():
    MAX_NUM = 10 ** 5
    Q = int(input())
    lr = [None] * Q
    for i in range(Q):
        lr[i] = tuple(map(int, input().split()))

    is_prime = [True] * (MAX_NUM + 1)
    is_prime[0] = False
    for i in range(4, MAX_NUM + 1, 2):
        is_prime[i] = False

    is_prime[1] = False
    for i in range(3, MAX_NUM + 1, 2):
        for j in range(3 * i, MAX_NUM + 1, 2 * i):
            is_prime[j] = False

    S = {}
    S[-1] = 0
    for i in range(1, MAX_NUM + 1, 2):
        if is_prime[i] and is_prime[(i + 1) // 2]:
            S[i] = S[i - 2] + 1
        else:
            S[i] = S[i - 2]

    for l, r in lr:
        print(S[r] - S[l - 2])


if __name__ == "__main__":
    main()
