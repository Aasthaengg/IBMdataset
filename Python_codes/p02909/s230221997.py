# 問題：https://atcoder.jp/contests/abc141/tasks/abc141_a

import sys

weather = ['Sunny', 'Cloudy', 'Rainy']
s = input()
if weather.count(s) < 1:
    sys.exit()
current_index = weather.index(s)
next_index = (current_index + 1) % 3
print(weather[next_index])

