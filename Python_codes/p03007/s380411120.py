import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    A = [int(a) for a in input().split()]
    A.sort()
    DP = [[None, None] for _ in range(N)]
    DP[0][0] = -A[0]
    DP[0][1] = -10 ** 20
    for i in range(1, N):
        DP[i][0] = DP[i-1][0] - A[i]
        DP[i][1] = max(DP[i-1][1] + A[i], DP[i-1][0] + A[i])
    print(DP[N-1][1])
    flip = N
    for i in reversed(range(1, N)):
        if DP[i][1] - DP[i-1][1] != A[i]:
            flip = i
            break
    else: flip = 1
    sumA = A[0]
    for i in range(flip, N-1):
        print(sumA, A[i])
        sumA -= A[i]
    print(A[N-1], sumA)
    sumA = A[N-1] - sumA
    for i in range(1, flip):
        print(sumA, A[i])
        sumA -= A[i]

    return 0

if __name__ == "__main__":
    solve()