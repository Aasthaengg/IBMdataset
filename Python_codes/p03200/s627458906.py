def resolve():
  S = input().strip()
  
  ans = 0
  n_black = 0
  for index, s in enumerate(S):
    if s == "B":
      ans += len(S) - index - 1 - n_black
      n_black += 1
  
  print(ans)
resolve()