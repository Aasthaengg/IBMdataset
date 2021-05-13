c = [[int(cn) for cn in input().split()] for _ in range(3)]
max_val = max(c[0])
ans = 'No'
for a1 in range(max_val + 1):
  b = [c[0][i] - a1 for i in range(3)]
  correct = True
  for i in range(2):
    ai_cand = []
    for j in range(3):
      cand = c[i + 1][j] - b[j]
      correct = cand >= 0
      if correct:
        ai_cand.append(cand)
      else:
        break
    correct = correct and (ai_cand[0] == ai_cand[1] and ai_cand[1] == ai_cand[2])
    if not correct:
      break
  if correct:
    ans = 'Yes'
    break
print(ans)
