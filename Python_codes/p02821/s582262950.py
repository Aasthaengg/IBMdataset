
from bisect import bisect_left, bisect_right
from itertools import accumulate
def resolve():
    def shake_cnt(x):
        cnt = 0
        pos = 0
        for i in range(N):
            pos = bisect_left(A, x - A[i])
            cnt += N - pos
        return cnt < M # X以上の和がM個未満かどうか

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    # 終了時にngにX-1,okにXが入っている。
    ng = 0
    ok = 10 ** 6
    while abs(ok - ng) > 1:
        mid = (ok + ng)//2
        if shake_cnt(mid):
            ok = mid
        else:
            ng = mid

    acc = [0] + list(accumulate(A))
    ans = 0
    for i in range(N):
        pos = bisect_right(A, ng - A[i])
        cnt = N - pos
        ans += cnt * A[i] + (acc[N] - acc[pos])
        M -= cnt
    ans += M * ng
    print(ans)


if __name__ == "__main__":
    resolve()
