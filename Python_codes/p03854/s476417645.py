S = input()
 
# 前から順に消すと詰む
# 後ろから順に消すと一意に定まる
while True:
  if S[-5:] == 'erase': S = S[:-5]
  else:
    if S[-6:] == 'eraser': S = S[:-6]
    else:
      if S[-5:] == 'dream': S = S[:-5]
      else:
        if S[-7:] == 'dreamer': S = S[:-7]
        else: break

if len(S) == 0: print('YES')
else: print('NO')