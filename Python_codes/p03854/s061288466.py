S =input()
ls_S = list(S)
ans = "YES"

while len(ls_S) != 0:
  if "".join(ls_S[len(ls_S)-5:]) == "dream":
    ls_S = ls_S[:len(ls_S)-5]
  elif "".join(ls_S[len(ls_S)-5:]) == "erase":
    ls_S = ls_S[:len(ls_S)-5]
  elif "".join(ls_S[len(ls_S)-7:]) == "dreamer":
    ls_S = ls_S[:len(ls_S)-7] 
  elif "".join(ls_S[len(ls_S)-6:]) == "eraser":
    ls_S = ls_S[:len(ls_S)-6]
  else:
    ans = "NO"
    break
print(ans)