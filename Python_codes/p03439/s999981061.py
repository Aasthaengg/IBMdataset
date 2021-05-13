N = int(input())


def query(i):
    print(i)
    s = input()
    if s == 'Vacant':
        exit()
    return s


root = query(0)


def is_ok(ind):
    # 左ならTrue
    response = query(ind)
    if ind % 2 == 1:
        return root == response
    else:
        return root != response


def bin_search_meguru():
    """
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng, okは,とり得る最小の値-1,とり得る最大の値+1
    """

    # 適当にいじる
    ng = -1  # ind=0が条件を満たすこともあるため
    ok = N  # ind=len(a)-1が条件を満たさないこともあるため

    # いじらない
    # okとngのどちらが大きいかわからないことを考慮
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return False


bin_search_meguru()
