def main():
    # import sys
    # # input = sys.stdin.readline
    # sys.setrecursionlimit(10 ** 9)
    # MOD = 10 ** 9 + 7


    S = tuple(input())
    x, y = map(int, input().split())

    N = 8010

    X = [0]
    Y = [0]
    flag = True
    for s in S:
        if s == 'F':
            if flag:
                X[-1] += 1
            else:
                Y[-1] += 1
        else:
            if flag:
                if Y[-1] != 0:
                    Y.append(0)
            else:
                if X[-1] != 0:
                    X.append(0)
            flag = not flag

    dp = [[0] * (2 * N) for _ in range(2)]
    if S[0] == 'F':
        dp[0][X[0] + N] = 1
    else:
        dp[0][X[0] + N] = 1
        dp[0][-X[0] + N] = 1

    for i in range(1, len(X)):
        x_ = X[i]
        for j in range(2 * N):
            dp[i % 2][j] = 0
            if j >= x_:
                if dp[(i - 1) % 2][j - x_]:
                    dp[i % 2][j] = 1
            if j + x_ < 2 * N:
                if dp[(i - 1) % 2][j + x_]:
                    dp[i % 2][j] = 1

    # print (dp)
    if dp[(len(X) - 1) % 2][x + N] == 0:
        print ('No')
        exit()

    dp = [[0] * (2 * N) for _ in range(2)]
    dp[0][Y[0] + N] = 1
    dp[0][-Y[0] + N] = 1

    for i in range(1, len(Y)):
        y_ = Y[i]
        for j in range(2 * N):
            dp[i % 2][j] = 0
            if j >= y_:
                if dp[(i - 1) % 2][j - y_]:
                    dp[i % 2][j] = 1
            if j + y_ < 2 * N:
                if dp[(i - 1) % 2][j + y_]:
                    dp[i % 2][j] = 1

    if dp[(len(Y)-1) % 2][y + N] == 0:
        print ('No')
        exit()

    print ('Yes')

if __name__ == '__main__':
    main()