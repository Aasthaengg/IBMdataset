S = input()
T = input()
sdic = {}
tdic = {}
flag = True
for s, t in zip(S, T):
  if s not in sdic:
    sdic[s] = t
  if t not in tdic:
    tdic[t] = s
  if sdic[s] != t or tdic[t] != s:
    flag = False
    break
if flag:
  print("Yes")
else:
  print("No")