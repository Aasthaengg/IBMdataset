n = int(input())
L = sorted(list(map(int, input().split())), reverse=True)
L.append(0)

def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    judge = L[i] < L[j] + L[arg]
#    print(judge, i, j, arg, L[i], L[j], L[arg])
    return judge

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

count = 0
for i in range(n):
    for j in range(i+1, n):
        k = meguru_bisect(n+1, j)
        if k > j:
            #print(i, j, k, L[i], L[j], L[k])
            count += k - j
print(count)
