s = input()
weather = ['Sunny', 'Cloudy', 'Rainy']
i = weather.index(s)
if (i == 0) | (i == 1):
    print(weather[i + 1])
else:
    print(weather[0])