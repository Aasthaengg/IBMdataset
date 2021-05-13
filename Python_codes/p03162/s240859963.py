import enum


def main():
    N = int(input())
    dp = [[] for _ in range(N)]
    for i in range(N):
        abc = list(map(int, input().split()))
        if i == 0:
            dp[0] = abc
        else:
            for k, v in enumerate(abc):
                vals = []
                for j in range(3):
                    if k != j:
                        vals.append(dp[i-1][j])
                dp[i].append(v + max(vals))

    print(max(dp[-1]))


if __name__ == '__main__':
    main()
