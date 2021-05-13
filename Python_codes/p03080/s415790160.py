people_number = int(input())
hat_str = input()
red_hat = hat_str.count("R")
if red_hat > (people_number/2):
  print("Yes")
else:
  print("No")
