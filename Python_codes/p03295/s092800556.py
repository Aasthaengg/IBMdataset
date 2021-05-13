N, M = map(int, input().split())
ab_list = []
for _ in range(M):
    a, b = map(int, input().split())
    ab_list.append((a, b))

# bについて昇順ソート
ab_list.sort(key=lambda x: x[1])

ans = 0

# 直前に切断した橋のindex
# 0や適当な負の値で初期化しておくと1回目の判定で都合が良い
pre_x = 0

for a, b in ab_list:
    # 直前の切断で条件が満たせる場合
    if pre_x >= a:
        continue
    # 新たに切断する必要がある場合
    else:
        pre_x = b - 1
        ans += 1
print(ans)
