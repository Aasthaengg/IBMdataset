N = int(input())
A = list(map(int, input().split()))
assets = 1000               # 資産

# 売買するかどうかのフラグ(買→1、売→0)をリストで生成
# (所持資産・所持株数を最大限に使い切って行う)
flag = []
for n in range(N-1):
    if A[n] <= A[n+1]:      # 当日の株価 <= 翌日の株価 ⇒ 買う
        flag.append(1)
    else:
        flag.append(0)      # 当日の株価 > 翌日の株価 ⇒ 売る
flag.append(0)              # 最終日は売る
# print(flag)

amount = 0                  # 所持株数
for idx, f in enumerate(flag):      # 売買処理
    if f == 1:
        purchase = assets // A[idx] # 購入数
        amount += purchase
        assets -= purchase * A[idx]
    else:
        assets += amount * A[idx]
        amount = 0
    # print(assets, amount)

print(assets)
