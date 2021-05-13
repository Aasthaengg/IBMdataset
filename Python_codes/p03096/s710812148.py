from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")

def main():
    md = 10 ** 9 + 7
    n = int(input())
    cc = [int(input()) for _ in range(n)]
    dp = [0] * (n + 1)
    dp[0] = 1
    ll = defaultdict(int)
    pc = -1
    for r, c in enumerate(cc):
        dp[r + 1] = dp[r]
        if c == pc: continue
        dp[r + 1] = (dp[r + 1] + ll[c]) % md
        ll[c] = (ll[c] + dp[r]) % md
        pc = c
    print(dp[n])

main()
