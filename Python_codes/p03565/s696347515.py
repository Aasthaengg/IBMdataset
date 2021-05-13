import copy
S_dash = input()
T = input()

len_S = len(S_dash)
len_T = len(T)

candidate0 = list(S_dash)


ans = "z"*51

if len_S >= len_T:
  for s in range(len_S):
    cha_S = S_dash[s]
    if cha_S != "?" and cha_S in list(T):
      for t in range(len_T):
        cha_T = T[t]
        if cha_S == cha_T and 0<= s-t < len_S and  0< s-t+len_T <= len_S:
          S_cut = S_dash[s-t:s-t+len_T]
          candidate1 = copy.deepcopy(candidate0)
          for x in range(len_T):
            if S_cut[x] == "?":
              candidate1[s-t+x] = T[x]
            elif  S_cut[x] != T[x]:
              break
          else:
            if "".join(candidate1[s-t:s-t+len_T]) == T:
              if ans > "".join(candidate1).replace('?', 'a'):
                ans = "".join(candidate1).replace('?', 'a')
  
  
  
  for u in range(len_S-len_T+1):
    cut_S = S_dash[u:u+len_T]
    if cut_S.count("?") == len_T:
      candidate1 = copy.deepcopy(candidate0)
      for t in range(len_T):
        candidate1[u+t] = T[t]
      if ans > "".join(candidate1).replace('?', 'a'):
        ans = "".join(candidate1).replace('?', 'a')
                
if ans == "z"*51:
  ans = "UNRESTORABLE"
print(ans)