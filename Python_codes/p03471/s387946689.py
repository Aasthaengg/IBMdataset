N, Y = map(int, input().split());

# 10000x + 5000y + 1000z = Y
# z = N - x - y
# → 9000x + 4000y = Y - 1000N

# Y - 1000N
flag = False;
S = Y - N * 1000;
for i in range(N + 1):
  y_div, y_mod = divmod((S - 9000 * i), 4000);
  z = N - i - y_div;
  if (y_mod == 0 and z >= 0 and y_div >= 0):
    print(str(i) + " " + str(y_div) + " " + str(z));
    flag = True;
    break;

if (flag == False):
  print("-1 -1 -1");