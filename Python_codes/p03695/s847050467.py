from collections import Counter
N = int(input())
a = [min(8, int(x) // 400) for x in input().split()]
cnt = Counter(a)

min_col = 0     # レート3200未満の人の色の数
for i in range(8):
    if cnt[i]:
        min_col += 1

if min_col == 0:  # 全員3200以上
    min_col = 1
    max_col = N
else:
    max_col = min_col + cnt[8]

print(min_col, max_col)