import sys
import bisect
input = lambda: sys.stdin.readline().rstrip()


def solve():

    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0 for _ in range(N + 1)]

    for i in range(N):
        S[i + 1] = S[i] + A[i] - 1

    d = dict()
    for i in range(N + 1):
        k = S[i] % K
        if k in d:
            d[k].append(i)
        else:
            d[k] = [i]

    # print(d)

    ans = 0
    for k, v in d.items():
        if len(v) <= 1:
            continue
        else:
            for i in range(len(v)):
                s = v[i] + K - 1
                si = bisect.bisect_right(v, s)
                ans += (si - i) - 1
                # print(i, si)

    print(ans)


if __name__ == '__main__':
    solve()
