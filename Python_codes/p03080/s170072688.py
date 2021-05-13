import sys
input_list = sys.stdin.readlines() 
N, s = map(str.strip, input_list)
red_hat_counter = 0
for s_str in s:
  if s_str == "R":
    red_hat_counter += 1
if red_hat_counter > (int(N)/2):
  print "Yes"
else:
  print "No"