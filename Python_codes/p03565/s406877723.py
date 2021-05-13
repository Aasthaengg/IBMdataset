S = str(input())
T = str(input())
index = []

for i in range(len(S) - len(T) + 1):
  if (S[i] != T[0]) and (S[i] != "?"):
    continue
  else:
    p = 0
    now = i
    j = 0
    index_i = -1
    while p == 0:
      if (S[now] != T[j]) and (S[now] != "?"):
        p = 1
      else:
        now += 1
        j += 1
      #print(now, j, len(T), index)
      if j == len(T):
        index_i = i
        p = 1
    if index_i != -1:
      index.append(index_i)
      
#print(index)
if (len(index) == 0):
  print("UNRESTORABLE")
else:
  ans_index = index[-1]
  ans = [0] * len(S)
  q = 0
  for i in range(len(S)):
    if i == ans_index:
      ans[i] = T[0]
      q = 1
    elif (q != 0):  
      ans[i] = T[q]
      q += 1
      if q == len(T):
        q = 0
    else:
      if S[i] != "?":
        ans[i] = S[i]
      else:
        ans[i] = "a"
    #print(ans, S)
  
  #print(ans) 
  #print(ans_index)
  for i in range(len(ans)):
    print(ans[i], end = "")
  print("")
  


