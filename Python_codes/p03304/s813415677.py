import sys

def solve():
    n, m, d = map(int, input().split())
    DP = [0] * m
    if d == 0: add = n
    else: add = d * 2 + 2 * (n - 2 * d)
    print((m - 1) * add / pow(n, 2))
    return 0

if __name__ == "__main__":
    solve()