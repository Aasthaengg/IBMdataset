import sys

input_list = sys.stdin.readlines() 
N, s = map(str.strip, input_list)

red_hat_counter = 0
blue_hat_counter = 0

for s_char in s:
  if s_char == "R":
    red_hat_counter += 1
  else:
    blue_hat_counter += 1

if red_hat_counter > blue_hat_counter :
  print("Yes")
else:
  print("No")