S = input()
S_list = list(S)
remain_match = 15 - len(S_list)
S_remain_win = 8 - S.count("o")
if remain_match >= S_remain_win:
  print("YES")
else:
  print("NO")
