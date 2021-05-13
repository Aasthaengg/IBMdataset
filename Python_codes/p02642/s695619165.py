#!python3

import sys
iim = lambda: map(int, sys.stdin.readline().rstrip().split())

def resolve():
    it = map(int, sys.stdin.read().split())
    N = next(it)
    A = [next(it) for i in range(N)]

    if N == 1:
        print(1)
        return

    ax = max(A)+1
    dp = [0]*ax
    for ai in A:
        da = dp[ai]
        if da > 1:
            continue
        dp[ai] += 1
        if da == 0:
            for aj in range(2*ai, ax, ai):
                dp[aj] = 2
    ans = 0
    for ai in A:
        if dp[ai] == 1:
            ans += 1
    print(ans)


if __name__ == "__main__":
    resolve()
