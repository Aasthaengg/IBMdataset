from collections import Counter

S = input()
S1 = S

st = set(S)
rlt = 1000

if len(Counter(st)) == 1:
  print(0)
  exit()
  
for s in st:
  S = S1
  t = 0
  while len(Counter(S)) > 1:
    tmp = ''
    for i in range(1,len(S)):
      if S[i-1] == s or S[i] == s:
        tmp += s
      else:
        tmp += S[i]
    t += 1
    S = tmp

  if t < rlt:
    rlt = t
    
print(rlt)