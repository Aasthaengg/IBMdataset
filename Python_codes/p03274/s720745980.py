import sys
import bisect


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    S = []
    ans = 10 ** 9 + 7

    start = bisect.bisect(X, 0)

    for i in range(min(start+1,K+1)):
        temp = 0
        if N - start < K-i:  #右にある個数が取るべき個数を超えたときはスキップ
            continue

        if i ==0:
            ans = min(X[start+K-1],ans)
            continue

        if i ==K:
            ans =min(-X[start-K],ans)
            continue
        # 左から
        temp += -X[start - i] * 2
        temp += X[start + K - i-1]
        ans = min(temp, ans)

        # 右から

        temp = X[start + K - i-1] * 2
        temp += -X[start - i]
        ans = min(temp, ans)





    print(ans)




if __name__ == "__main__":
    main()
