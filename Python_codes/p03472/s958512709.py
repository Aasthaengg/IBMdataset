n, h = map(int, input().split())

ab = [list(map(int, input().split())) for _ in range(n)]
a_max = sorted(ab, key=lambda x: x[0], reverse=True)[0][0]
ab_sorted = sorted(ab, key=lambda x: x[1], reverse=True)

ans = 0
# a_maxよりも高い攻撃力の刀を投げつける
for i in range(n):
    if a_max > ab_sorted[i][1]:
        break
    h = h - ab_sorted[i][1]
    ans += 1
    if h <= 0:
        print(ans)
        exit(0)

# 引き算だとめっちゃ時間がかかるので割り算で斬りかかる数を求める
add = h//a_max if h % a_max == 0 else h//a_max + 1
print(ans + add)