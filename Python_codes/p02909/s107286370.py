# 入力の取得
S = input()

# 入力内容から次の天気を予測
if S == "Sunny":
    print("Cloudy")
elif S == "Cloudy":
    print("Rainy")
elif S == "Rainy":
    print("Sunny")
else:
    print("入力内容が間違っています。")