# A - Weather Prediction
# 1日毎に　晴れ（Sunny） 曇り（Cloudy） 雨（Rainy） の順に変化する
# 晴 → 曇 → 雨 → 晴 → 曇 → 雨 → ...

# 文字列 S の入力
S = input()
# print(S)

# 明日の天気を表示させる
# 今日の天気で分岐し、printで表示
if S == 'Sunny':
    # print('Cloudy')
    answer = 'Cloudy'
elif S == 'Cloudy':
    # print('Rainy')
    answer = 'Rainy'
elif S == 'Rainy':
    # print('Sunny')
    answer = 'Sunny'

print(answer)
