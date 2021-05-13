S = list(input())
L = len(S)

if L != 26:
  # まだ使ってないもので、最大ものもを最後につける
  USED = [False] * 26
  for s in S:
    USED[ord(s) - 97] = True
  
  for i in range(26):
    if not USED[i]:
      S.append(chr(97+i))
      break
  
  print("".join(S))
else:
  # 26文字ある場合
  prev = -1
  k = -1
  USED = []
  for i in range(26)[::-1]:
    d = ord(S[i]) - 97
    if prev < d:
      prev = d
      USED.append(S[i])
    else:
      k = i
      break
  
  if k == -1:
    print(-1)
  else:  
    nxt = min([s for s in USED if s > S[k]])
    S = S[:k] + [nxt]
    print("".join(S))
