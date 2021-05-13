line = input()
rain_day = 0
k = 0
for wether in line:
  #当日雨
  if wether == "R":
    rain_day += 1
  #当日晴れ、前日は雨
  elif rain_day != 0:
    k = rain_day
    rain_day = 0
  #当日晴れ、前日も晴れ
  else:
    pass
if k > rain_day:
  print(k)
else:
  print(rain_day)