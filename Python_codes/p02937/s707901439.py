from bisect import bisect_left
S = input()
T = input()

set_s = set(S)
set_t = set(T)
len_t = len(T)
if len(set_s & set_t) != len(set_t):
  print(-1)  
else:  
  dic = {c:[] for c in set_s}
  dic_len = {}
  for i,s in enumerate(S):
    dic[s].append(i)
    
  for k in dic:
    dic_len[k] = len(dic[k])
  
  si = 0
  cnt = 0
  for t in T:    
    i = bisect_left(dic[t],si)
    if i == dic_len[t]:
      si = 0
      cnt += 1
      i = bisect_left(dic[t],si)
        
    if dic[t][i] == si:
      si += 1
    else:      
      si = dic[t][i] + 1
              
  print(cnt * len(S) + si)