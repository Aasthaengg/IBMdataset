import sys
from itertools import accumulate

input = sys.stdin.readline


def main():
    N, M, Q = map(int, input().split())
    LR = [None] * M
    for i in range(M):
        LR[i] = tuple(map(int, input().split()))
    pq = [None] * Q
    for i in range(Q):
        pq[i] = tuple(map(int, input().split()))

    S = [[0] * (N + 1) for _ in range(N + 1)]
    for L, R in LR:
        S[L][R] += 1
    for i in range(N + 1):
        S[i] = list(accumulate(S[i]))

    ans = [0] * Q
    for i, (p, q) in enumerate(pq):
        for j in range(p, q + 1):
            ans[i] += S[j][q] - S[j][p - 1]

    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
