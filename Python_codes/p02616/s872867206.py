
def resolve():
    MOD = 10**9+7
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    P = []
    M = []
    for a in A:
        if a < 0:
            M.append(a)
        else:
            P.append(a)
    p_n = len(P)
    m_n = len(M)
    # 正の値にできるかを判定する
    ok = False
    if p_n > 0:
        if N == K:
            ok = (m_n%2==0) # 負の値が偶数あるとTrue
        else:
            ok = True
    # 負の値しか無い場合
    else:
        ok = (K % 2 == 0) # Kが偶数なら負の値を偶数個選べる

    ans = 1
    # 正の値にできない
    if not ok:
        # 絶対値が小さい順にソート
        A.sort(key=lambda x:abs(x))
        for i in range(K):
            ans *= A[i]
            ans %= MOD
    else:
        P.sort()
        M.sort(reverse=True)
        if K%2== 1:
            ans *= P.pop()
            ans %= MOD
        pair = []
        # 2個ずつ処理する
        while len(P) >= 2:
            x = P.pop()
            x *= P.pop()
            pair.append(x)
        while len(M) >= 2:
            x = M.pop()
            x *= M.pop()
            pair.append(x)
        pair.sort(reverse=True)
        for i in range(K//2):
            ans *= pair[i]
            ans %= MOD
    ans %= MOD
    print(ans)

if __name__ == "__main__":
    resolve()
