def submit():
    n, m, q = map(int, input().split())
    rng = {i: [0 for _ in range(n + 1 - i)] for i in range(1, n + 1)}
    for _ in range(m):
        l, r = map(int, input().split())
        rng[l][r - l] += 1
    
    for i in range(1, n + 1):
        for j in range(n - i):
            rng[i][j + 1] += rng[i][j]

    ans = []
    for _ in range(q):
        pl, pr = map(int, input().split())
        # plから始まり, pr - pl以下で終わる列車を数える
        cnt = 0
        for i, ppl in enumerate(range(pl, pr + 1)):
            cnt += rng[ppl][pr - pl - i]
        ans.append(cnt)

    for a in ans:
        print(a)
            

submit()