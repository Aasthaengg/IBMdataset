# 高橋君の住む町の天気は、一日ごとに晴れ(Sunny)、くもり(Cloudy)、雨(Rainy)、晴れ、くもり、雨、… と周期的に変化します。
# 今日の天気を表す文字列 S が与えられるので、明日の天気を予測してください。

# 標準入力から明日の天気を表す文字列 S を取得する
today_weather = input()
tommorow_weather = 'I do not know. Sorry!!'

# 取得した入力 S を条件に従い出力する。
if today_weather == 'Sunny':
    tommorow_weather = 'Cloudy'
elif today_weather == 'Cloudy':
    tommorow_weather = 'Rainy'
elif today_weather == 'Rainy':
    tommorow_weather ='Sunny'

print(tommorow_weather)
