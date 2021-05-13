S = input()
weather = ['Sunny', 'Cloudy', 'Rainy']
num = weather.index(S)
ans_index = num + 1
if ans_index == 3:
    ans_index = 0
print(weather[ans_index])