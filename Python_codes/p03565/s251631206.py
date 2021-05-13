S = list(input())
T = list(input())
ans_list = []
for i in range(len(S)):
  flag = True
  if S[i] == "?" or S[i] == T[0]:
    tmp = S[i:i+len(T)]
    if len(tmp) != len(T):
      continue
    for j in range(len(T)):
      if tmp[j] != '?' and T[j] != tmp[j]:
        flag = False
        break
    if flag:
      ans = S[:i] + T + S[i+len(T):]
      for i in range(len(ans)):
        if ans[i] == '?':
          ans[i] = 'a'
      ans_list += [ans]

if len(ans_list) != 0:
  ans_list = sorted(ans_list)
  print(''.join(ans_list[0]))
else:
  print('UNRESTORABLE')

