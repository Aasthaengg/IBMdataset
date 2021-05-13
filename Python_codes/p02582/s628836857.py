D = input()
ans = 0
ans_list = []
if D.count("R") >= 1:
  for i in range(3):
    if D[i] == 'R':
      ans += 1
      ans_list.append(ans)
    elif D[i] == 'S':
      ss = 0
      ans_list.append(ss)
      if i > 0:
        ans = 0
  print(max(ans_list))
elif D.count("R") < 1:
  print(0)
