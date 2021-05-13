n, k = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
F = list(int(x) for x in input().split())
A.sort()
F.sort(reverse=True)

def meguru_bisect(ng, ok):
    """
    初期値のng,okを受け取り, check=>Trueを満たす最大値(最小値)を返す
    条件を満たす最大値を求める場合、初期値は(ng:上限の外, ok:下限の外)   例) 10**9+1, -1
    条件を満たす最小値を求める場合、初期値は(ng:下限の外, ok:上限の外)   例) -1, 10**9+1
    上限の外や下限の外が返ってくる場合は条件を満たす値が範囲内になかったことを示すので、例外処理が必要
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    return ok

def check(x):
    tmp = 0
    for i in range(n):
        if A[i] * F[i] > x:
            tmp += A[i] - (x // F[i])
    return tmp <= k

ans = meguru_bisect(-1, 10**12 + 1)
print(ans)
