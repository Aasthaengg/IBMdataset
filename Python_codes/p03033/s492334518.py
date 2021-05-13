from bisect import bisect_left, bisect_right
from operator import itemgetter
import sys
input = sys.stdin.readline


def main():
    N, Q = map(int, input().split())
    constructions = [None] * N
    for i in range(N):
        S, T, X = map(int, input().split())
        constructions[i] = (S, T, X)
    constructions.sort(key=itemgetter(2))
    D = [int(input()) for _ in range(Q)]
    ans = [-1] * Q
    nxt = list(range(1, Q+1))
    for S, T, X in constructions:
        l = bisect_left(D, S-X)
        r = bisect_right(D, T-X-1)
        idx = l
        while idx < r:
            if ans[idx] == -1:
                ans[idx] = X
            nidx = nxt[idx]
            nxt[idx] = max(nxt[idx], r)
            idx = nidx
    for a in ans:
        print(a)


if __name__ == "__main__":
    main()
