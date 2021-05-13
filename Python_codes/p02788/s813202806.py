def binary_search(v, is_ok):
    """
    ソートしてから使え！！！
    v : list
        ある場所から左が条件を満たさず、右が条件を満たすように並んだ配列
    is_ok(x) : bool
        vの要素xが条件を満たすかどうかを返す関数
    """
    ng = -1             # 条件を満たさないiのうち今わかっている中で最大の値(v[0]が条件を満たすかもしれないので-1から)
    ok = len(v)         # 条件を満たすiのうち今わかっている中で最小の値(v[n-1]が条件を満たさないかもしれないのでnから)
    # okをできるだけ左に移動させてreturnする

    # ...... ng ok ......
    #          | ->
    # こうなるまで
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2

        if is_ok(v[mid]):   # v[mid]はokであることがわかった
            ok = mid        # okを左に移動
        else:               # v[mid]はngであることがわかった
            ng = mid        # ngを右に移動

    return ok



N, D, A = map(int, input().split())
XH = [tuple(map(int, input().split())) for i in range(N)]
XH.sort()
X = [x for x, h in XH]
H = [(h + A - 1) // A for x, h in XH]

yuukou = 0
mou_mukou = [0] * N + [0]
ans = 0

# lを左端としてn個爆弾を使う
def bomb(l, n):
    global ans, yuukou
    ans += n
    yuukou += n
    r = l + 2 * D
    mou_mukou[binary_search(X, lambda x: r < x)] += n

for i in range(N):
    yuukou -= mou_mukou[i]
    H[i] -= yuukou
    if H[i] > 0:
        bomb(X[i], H[i])

print(ans)
