import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    M = [1]
    for i in range(1, 12):
        if pow(6, i) > N: break
        M.append(pow(6, i))
    for i in range(1, 10):
        if pow(9, i) > N: break
        M.append(pow(9, i))
    M.sort()

    DP = [100000] * (N + 1)
    DP[N] = 0
    for i in reversed(range(N + 1)):
        if DP[i] < 100000:
            for m in M:
                if i - m >= 0: DP[i-m] = min(DP[i-m], DP[i] + 1)
    print(DP[0])

    return 0

if __name__ == "__main__":
    solve()