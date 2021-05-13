from sys import stdin
input = stdin.buffer.readline

def main():
    n, m, q = map(int, input().split())

    # Two-dimensional Cumulative Sum
    cs = [[0] * (n+1) for _ in range(n+1)]

    for _ in range(m):
        l, r = map(int, input().split())
        cs[l][r] += 1

    for l in range(1, n+1):
        for r in range(1, n+1):
            cs[l][r] += cs[l][r-1]
        for r in range(1, n+1):
            cs[l][r] += cs[l-1][r]

    ans = [-1] * q
    for lap in range(q):
        l, r = map(int, input().split())
        ans[lap] = cs[n][r] - cs[l-1][r]

    for i in ans:
        print(i)

main()