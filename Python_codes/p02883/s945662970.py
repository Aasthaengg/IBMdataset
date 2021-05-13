
def resolve():
    # 達成スコアを決める
    # 修行回数がK以下を達成できるスコアを二分探索
    def check(X):
        cnt = 0
        for i in range(N):
            a = X // F[i]
            if a < A[i]:  # 修行をしてスコアを最小化する
                cnt += A[i] - a
        return cnt <= K

    N, K = map(int, input().split())
    A = sorted(map(int, input().split()))
    F = sorted(map(int, input().split()), reverse=True)

    ok = 10 ** 12 # 最大スコア a: 10**6 * x:10**6
    ng = -1
    while ok - ng > 1:
        X = (ok + ng) // 2
        if check(X):
            ok = X
        else:
            ng = X

    print(ok)


if __name__ == "__main__":
    resolve()
