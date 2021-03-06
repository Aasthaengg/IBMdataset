from collections import Counter

H, W, N = map(int, input().split())

# 3*3マスの処理用リスト
dir = [[0, 0], [1, 0], [1, 1], [0, 1], [-1, 1],
       [-1, 0], [-1, -1], [0, -1], [1, -1]]

# そのマスを中心とする3*3グリッドに含まれる黒マスの数
dict = {}

for i in range(N):
    a, b = map(int, input().split())
    for dy, dx in dir:
        # 3*3グリッドは、H*Wの中に完全に含まれていなければならないことに注意
        if 2 <= a + dy <= H - 1 and 2 <= b + dx <= W - 1:
            if (a + dy, b + dx) not in dict:
                dict[(a + dy, b + dx)] = 1
            else:
                dict[(a + dy, b + dx)] += 1

c = Counter(dict.values())
ans = [0 for _ in range(10)]

# ans[1], ans[2], ..., ans[9]を確定させる（ans[0]は後述）
for k, v in c.items():
    if v > 0:
        ans[k] = v

# 全体で作れる3*3グリッドは(H-2)*(W-2)個
# ans[1],...,ans[9]の総和を引くとans[0]になる
ans[0] = (H - 2) * (W - 2) - sum(ans[1:])

for i in range(10):
    print(ans[i])
