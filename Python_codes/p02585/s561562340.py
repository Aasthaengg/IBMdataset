def d_moving_piece():
    N, K = [int(i) for i in input().split()]
    P = [int(i) - 1 for i in input().split()]  # マスの番号は 0-indexed とする
    C = [int(i) for i in input().split()]

    # 順列をサイクルごとに分解
    is_visited = [False] * N
    cycles = []  # サイクルごとのスコアを記録
    for i in range(N):
        if is_visited[i]:
            continue

        current = i
        t = []
        while not is_visited[current]:
            is_visited[current] = True
            t.append(C[current])
            current = P[current]
        cycles.append(t)

    ans = -float('inf')
    for s in cycles:
        m = len(s)

        # サイクルを 2 周したものの累積和
        total = [0] * (2 * m + 1)
        for i in range(2 * m):
            total[i + 1] = total[i] + s[i % m]

        reminder = [-float('inf')] * m  # [r]: 連続する r 個の和の最大値
        for i in range(m):
            for j in range(m):
                reminder[j] = max(reminder[j], total[i + j] - total[i])

        # 「余り」の長さで場合分け
        for r in range(m):
            if r > K:
                continue  # 移動できる回数より多く動いたことになり、矛盾

            q = (K - r) // m  # この回数だけサイクルを 1 周する
            if r == 0 and q == 0:
                continue  # 動いていないので、除外

            if total[m] > 0:
                # 周回したほうが得なので、可能な限り周回する
                ans = max(ans, reminder[r] + total[m] * q)
            elif r > 0:
                # 周回すると損なので、必要なだけ (r 回) 移動したら終わる
                ans = max(ans, reminder[r])
    return ans

print(d_moving_piece())
