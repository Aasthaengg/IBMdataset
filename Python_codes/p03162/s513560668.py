from copy import deepcopy


def solve(N, abc):
    dp = [[0, 0, 0] for i in range(N+1)]

    for i in range(1, N+1):
        for j in range(3):
            tmp = deepcopy(dp[i-1])
            tmp.pop(j)
            dp[i][j] = max(tmp) + abc[i-1][j]

    return(max(dp[N]))


if __name__ == "__main__":
    N = int(input())
    abc = [list(map(int, input().split())) for _ in range(N)]
    print(solve(N, abc))
