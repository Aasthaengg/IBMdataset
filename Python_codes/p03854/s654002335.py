S = input()
S = S[::-1]
candidacies = ["dream", "dreamer", "erase", "eraser"]
candidacies = [c[::-1] for c in candidacies]

fi_flg = False
while fi_flg is False:
  if S[:7] in candidacies:
    S = S[7:]
  elif S[:6] in candidacies:
    S = S[6:]
  elif S[:5] in candidacies:
    S = S[5:]
  else:
    fi_flg = True

if len(S) == 0:
  print("YES")
else:
  print("NO")