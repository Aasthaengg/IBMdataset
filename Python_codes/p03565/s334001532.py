S_ = input()
T = input()

if len(S_) < len(T):
  print('UNRESTORABLE')
  exit()

i_ = -1

for i in range(len(S_)-len(T)+1):
  for j in range(len(T)):
    if S_[i+j] != T[j] and S_[i+j] != '?':
      break
    if j == len(T) - 1:
      i_ = i

if i_ == -1:      
  print('UNRESTORABLE')
else: 
  if i_ + len(T) == len(S_):
    print(S_[:i_].replace('?','a')+T)
  else:
    print(S_[:i_].replace('?','a')+T+S_[i_+len(T):].replace('?','a'))