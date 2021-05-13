import sys
a, b, c, d = list(input())

bit = 4

for i in range(8):
  calc_list = []
  for j in range(3):
    if((i >> j) & 1):
      calc_list.append("+")
    else:
      calc_list.append("-")
  calc_str = a + calc_list[0] + b + calc_list[1] + c + calc_list[2] + d
  if eval(calc_str) == 7:
    print(calc_str + "=7")
    sys.exit()