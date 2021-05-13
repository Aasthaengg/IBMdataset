N = int(input())
# ソートすればアナグラムは同じ文字列になる
s = [str(sorted(input())) for i in range(N)]

ans = 0

# 既に見た文字列 : 累計出現回数
cnt = {}

for i in range(N):
    # 既に見た文字列の場合
    if s[i] in cnt:
        # 既にn個ある時、新しく1個増えると組み合わせはn通り増える
        ans += cnt[s[i]]
        cnt[s[i]] += 1
    # 始めて見る文字列
    else:
        cnt[s[i]] = 1

print(ans)
