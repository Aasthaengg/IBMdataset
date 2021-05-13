S = input()
t = input()

n = len(S)
m = len(t)

for i in range(n-m, -1, -1):
  t_ = S[i:i+m]
  for j in range(m+1):
    if j == m:
      print((S[:i] + t + S[i+m:]).replace('?', 'a'))
      exit()
    if t_[j] == '?':
      continue
    elif t_[j] != t[j]:
      break
  
print('UNRESTORABLE')