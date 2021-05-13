

S = input()


week = {
  "MON": 1,
  "TUE": 2,
  "WED": 3,
  "THU": 4,
  "FRI": 5,
  "SAT": 6
}

if S == "SUN":
  print(7)
else:
  print(7 - week[S])
