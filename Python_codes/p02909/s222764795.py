S = input()
weather = ["Sunny", "Cloudy", "Rainy"]
a = weather.index(S)
print(weather[(a+1)%3])
