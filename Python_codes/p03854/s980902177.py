S = list(input())
while True:
  if len(S) >= 8:
    if S[:8] == ["d", "r", "e", "a", "m", "e", "r", "a"]:
      del S[:5]
    elif S[:7] == ["d", "r", "e", "a", "m", "e", "r"]:
      del S[:7]
    elif S[:6] == ["e", "r", "a", "s", "e", "r"]:
      del S[:6]
    elif S[:5] == ["d", "r", "e", "a", "m"]:
      del S[:5]
    elif S[:5] == ["e", "r", "a", "s", "e"]:
      del S[:5]
    else:
      print("NO")
      break
  elif len(S) == 7:
    if S[:7] == ["d", "r", "e", "a", "m", "e", "r"]:
      del S[:7]
  elif len(S) == 6:
    if S[:6] == ["e", "r", "a", "s", "e", "r"]:
      del S[:6]
  elif len(S) == 5:
    if S[:5] == ["d", "r", "e", "a", "m"]:
      del S[:5]
    elif S[:5] == ["e", "r", "a", "s", "e"]:
      del S[:5]
  elif len(S) == 0:
    print("YES")
    break
  else:
    print("NO")
    break
