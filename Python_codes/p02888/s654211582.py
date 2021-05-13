def is_ok(a,b,c):
    return L[a] < L[b] + L[c]
def meguru_bisect(ng, ok, a, b):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(a, b, mid):
            ok = mid
        else:
            ng = mid
    return ok
N = int(input())
L = sorted(list(map(int, input().split())), reverse=True)
ans = 0
for a in range(N):
    for b in range(a+1, N):
        ans += meguru_bisect(N,b,a,b)-b
print(ans)
