import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    X = [int(x) for x in input().split()]
    Xsub = sorted(X)
    midl, midr = Xsub[(N - 1) // 2], Xsub[N // 2]
    ans = [0] * N
    for i, x in enumerate(X):
        if x <= midl: ans[i] = midr
        else: ans[i] = midl
    print(*ans, sep="\n")

    return 0

if __name__ == "__main__":
    solve()