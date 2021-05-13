S = input()

point = 0
can_p_cnt = 0
for i in range(len(S)):
  if S[i] == 'g':
    if can_p_cnt > 0:
      #p
      point += 1
      can_p_cnt -= 1
    else:
      #g
      can_p_cnt += 1
  else:
    if can_p_cnt > 0:
      can_p_cnt -= 1
    else:
      point -= 1
      can_p_cnt += 1
      
print(point)