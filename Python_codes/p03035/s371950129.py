age, max_money = map(int, input().split())
if age>= 13:
  print(max_money)
elif age>=6 and age<=12:
  print(max_money//2)
elif age<=5:
  print("0")