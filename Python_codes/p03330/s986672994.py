N, C = map(int, input().split())
# D[i][j] = 色をiからjに変える時の「違和感」 = 「コスト」
D = [list(map(int, input().split())) for _ in range(C)]
# 最初の色
c = [list(map(int, input().split())) for _ in range(N)]

# cnt[i][j] = 初期状態において、(x+y)%3==iで、色がj(0,1,...,C-1)の数
cnt = [[0 for _ in range(C)]for _ in range(3)]
# グリッド全体(N*N)を調べる
for i in range(1, N + 1):
    for j in range(1, N + 1):
        cnt[(i + j) % 3][c[i - 1][j - 1] - 1] += 1
# print(cnt)

ans = 10**18

# (x+y)%3==0,1,2をc0,c1,c2で塗る
for c0 in range(C):
    for c1 in range(C):
        for c2 in range(C):
            # 同じ色があってはならない
            if c0 == c1 or c1 == c2 or c2 == c0:
                continue

            cost = 0
            # (x+y)%3==0 をc0に塗り替える
            for i, n in enumerate(cnt[0]):
                cost += n * D[i][c0]
            # (x+y)%3==1 をc1に塗り替える
            for i, n in enumerate(cnt[1]):
                cost += n * D[i][c1]
            # (x+y)%3==2 をc2に塗り替える
            for i, n in enumerate(cnt[2]):
                cost += n * D[i][c2]

            ans = min(ans, cost)

print(ans)
