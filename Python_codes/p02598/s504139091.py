n,k = map(int,input().split())
ls = list(map(int,input().split()))
#二分探索
#適切にokとngを定めていきましょう
def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    num = 0
    for i in range(n):
        num += -(-ls[i] // arg) -1
    if num <= k:
        return True
    return False
def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok
print(meguru_bisect(0, max(ls)+1))
