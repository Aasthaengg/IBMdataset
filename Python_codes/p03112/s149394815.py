import sys
from bisect import bisect_left


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)


def main():
    A, B, Q = map(int, input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]

    for i in range(Q):
        x = int(input())
        s_index = bisect_left(S, x)
        if s_index == 0:
            S1 = S[s_index]
            S2 = S[s_index]
        elif s_index == A:
            S1 = S[s_index - 1]
            S2 = S[s_index - 1]
        else:
            S1 = S[s_index]
            S2 = S[s_index - 1]

        t_index = bisect_left(T, x)
        if t_index == 0:
            T1 = T[t_index]
            T2 = T[t_index]
        elif t_index == B:
            T1 = T[t_index - 1]
            T2 = T[t_index - 1]
        else:
            T1 = T[t_index]
            T2 = T[t_index - 1]
        answer = float("inf")
        for s in [S1, S2]:
            for t in [T1, T2]:
                r = min(abs(x - s) + abs(t - s), abs(x - t) + abs(t - s))
                if answer > r:
                    answer = r
        print(answer)


if __name__ == "__main__":
    main()
