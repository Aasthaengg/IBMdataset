# 周期的にループする明日の天気を予測してください

# ループする関数がわからんかったから調べた
# 結果　ループする必要なし

# for (変数名）in (イテラブル）:
#    （コードブロック）

today = input ()

if today == "Sunny":
    print("Cloudy")
elif today == "Cloudy":
    print("Rainy")
else:
    print("Sunny")

