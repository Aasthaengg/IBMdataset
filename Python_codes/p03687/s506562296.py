S = input()
uni_s = list(set(list(S)))

ans = len(S) - 1

# -1,1
for s in uni_s:
  L = len(S)
  T = list(S)
  all_same = [s == t for t in S]
  cnt = 0
  while not all(all_same):
    cnt += 1
    newT = [False] * (L-1)
    for i in range(L):
      t = T[i]
      if s == t:
        if i < L-1:
          newT[i] = t
        if 0 <= i-1:
          newT[i-1] = t
      else:
        if i < L-1 and not newT[i]:
          newT[i] = t
        if 0 <= i-1 and not newT[i-1]:
          newT[i-1] = t
    
    all_same = [s==t for t in newT]
    T = newT
    L = len(T)
  ans = min(ans,cnt)

print(ans)
      
    
