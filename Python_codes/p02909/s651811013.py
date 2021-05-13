# 今日の天気を入力
today_weather = input()

# 今日の天気から明日の天気をSunny,Cloudy,Rainyの周期で予測して出力
if today_weather == "Sunny":
    print("Cloudy")
elif today_weather == "Cloudy":
    print("Rainy")
else:
    print("Sunny")