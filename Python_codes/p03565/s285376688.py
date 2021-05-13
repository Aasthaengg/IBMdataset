from copy import deepcopy
S = input()
T = input()
s_num = len(S)
t_num = len(T)
ans = []
if s_num < t_num:
  print('UNRESTORABLE')
else:
  for i in range(s_num-t_num+1):
    s_key = S[i:i+t_num]
    judge = 0
    for s, t in zip(s_key, T):
      if s=='?':
        judge += 1
      elif s == t:
        judge += 1
    if judge == t_num:
      tmp = S[:i] + T + S[i+t_num:]
      tmp = tmp.replace('?', 'a')
      ans.append(tmp)
  if ans:
    print(sorted(ans)[0])
  else:
    print('UNRESTORABLE')