n = int(input())
f = [list(map(int, input().split())) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(n)]

ans = -float('inf')
for bit in range(1, 2 ** 10):
    # 1店舗ずつを処理
    score = 0
    for i in range(len(f)):
        # 曜日・時刻ごとのスコアを計算
        cnt = 0
        for j in range(10):
            # ある店舗のi番目の時刻と、bitが合致するかチェック
            if f[i][j] & (bit >> j):
                cnt += 1
        score += p[i][cnt]
    ans = max(score, ans)
print(ans)