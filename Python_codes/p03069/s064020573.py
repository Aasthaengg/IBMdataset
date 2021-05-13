def tenka1bc19_c():
    N = int(input())
    S = str(input())

    # 白と黒の累積個数
    wt = [0]
    bk = [0]
    for s in S:
        w, b = wt[-1], bk[-1]
        if s == '.': w += 1
        else: b += 1
        wt.append(w)
        bk.append(b)

    # i番目までを白にして、i+1番目以降を黒にするときのコスト
    ans = 10**9
    for i in range(N+1):
        flip = bk[i] + wt[-1] - wt[i]
        ans = min(flip, ans)
    print(ans)

tenka1bc19_c()