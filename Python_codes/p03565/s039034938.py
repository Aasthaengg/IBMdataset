S = str(input())
T = str(input())

s = len(S)
t = len(T)
if s < t:
  flag = False
else:
  for i in range(s-t+1):
    num = s-t-i
    tmp = S[num:num+t]
    flag = True
    for j in range(t):
      if (tmp[j]!='?') and (T[j]!=tmp[j]):
        flag = False
        break
    if flag:
      if 0 < num < s-t:
        ans = S[:num] + T + S[num+t:]
      elif num == 0:
        ans = T + S[num+t:]
      else:
        ans = S[:num] + T
      break
    
if flag:
  ans = ans.replace('?', 'a')
  print(ans)
else:
  print('UNRESTORABLE')