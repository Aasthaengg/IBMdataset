#   AtCoder abc087 a
#   ストレッチ課題

#   入力
balance = int(input())
price_cake = int(input())
price_doughnut = int(input())

#   処理
# balance = balance - price_cake      # ケーキ購入後の残高
# balance = balance % price_doughnut  # ドーナツ購入後の残高
balance = (balance - price_cake) % price_doughnut

#   出力
print(balance)

