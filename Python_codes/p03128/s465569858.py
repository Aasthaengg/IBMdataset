import sys

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = [int(a) for a in input().split()]
    use = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    U = dict()
    for a in A:
        if use[a] in U: U[use[a]] = max(a, U[use[a]])
        else: U[use[a]] = a

    DP = [-1] * (N + 1)
    DP[0] = 0
    for i in range(N):
        if DP[i] > -1:
            for key in U:
                if i + key <= N:
                    DP[i + key] = max(DP[i + key], DP[i] * 10 + U[key])
    print(DP[N])

    return 0

if __name__ =="__main__":
    solve()