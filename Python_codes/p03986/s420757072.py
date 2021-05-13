x = input()
t_num = 0
s_num = 0
total = 0
for i in range(len(x)):
  if x[i] == 'S' and t_num == 0:
    s_num += 1
  elif x[i] == 'T':
    t_num += 1
  elif x[i] == 'S' and t_num > 0:
    total += min(s_num, t_num) * 2
    if s_num >= t_num:
      s_num = 1 + s_num - t_num
      t_num = 0
    else:
      s_num = 1
      t_num = 0
total += min(s_num, t_num) * 2
ans = len(x) - total
print(ans)