#atcoder template
def main():
    import sys
    imput = sys.stdin.readline
    #ここにコード
    #input
    from collections import Counter
    import itertools
    N = int(input())

    dp = [[0, 0] for _ in range(N)]
    for i in range(N):
        S = str(input())
        T = []
        for s in S:
            if s == "(":
                T.append(1)
            else:
                T.append(-1)
        x = list(itertools.accumulate(T))[-1]
        y = min(itertools.accumulate(T))
        dp[i] = [x, y]


    #output
    dp1 = [[x, y] for x, y in dp if x >= 0]
    dp2 = [[x, y] for x, y in dp if x < 0]
    dp1 = sorted(dp1, key = lambda x:x[1], reverse = True)
    dp2 = sorted(dp2, key = lambda x:x[0]-x[1], reverse = True)
    dp = dp1 + dp2

    checker = 0
    for p in dp:
        if checker + p[1] < 0:
            print("No")
            exit()
        checker += p[0]

    if checker == 0:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()