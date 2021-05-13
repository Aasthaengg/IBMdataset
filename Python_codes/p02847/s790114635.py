s = input()
days = ["SUN","MON","TUE","WED","THU","FRI","SAT"]

for i in range(len(days)):
  if days[i] == s:
    print(7 - i)