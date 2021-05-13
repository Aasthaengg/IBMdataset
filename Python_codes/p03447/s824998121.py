# A - Buying Sweets


# 所持金 X 円
# ケーキ屋のケーキの値段 A 円
# ドーナツ屋のドーナツの値段 B 円

X = int(input())
A = int(input())
B = int(input())

# print(X, A, B)

# ケーキ屋で 1 つ　ケーキを買う
balance_cake = X - A
# print(balance_cake)

# ドーナツ屋で １つ B円のドーナツをたくさん買いました
# balance_cake 円 で ドーナツを何個買えるか計算

max_purchase_donut = balance_cake // B
# print(max_purchase_donut)

# ドーナツ屋で購入した分引く　⇔ 残金
answer = balance_cake - (max_purchase_donut * B)
# print(answer)

# 残金を表示
print(answer)
