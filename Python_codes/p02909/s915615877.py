weather = ['Sunny', 'Cloudy', 'Rainy']
S = input()
idx = weather.index(S)
print(weather[(idx+1) % 3])