X = input()
s_cnt, t_cnt = 0, 0
for i in range(len(X)):
  if X[i] == "S":
    s_cnt += 1
  elif s_cnt != 0:
    s_cnt -= 1
    t_cnt += 1
print(len(X) - 2*t_cnt)