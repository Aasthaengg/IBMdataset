S = input()
T = input()

sts = set(S)
stt = set(T)

for i in range(26):
  c = chr(ord('a')+i)
  idx1 = [i for i, x in enumerate(T) if x == c]
  st1 = set([])
  idx2 = [i for i, x in enumerate(S) if x == c]
  st2 = set([])
  
  for j in idx1:
    if S[j] not in st1 and len(st1) > 0:
      print('No')
      exit()
    elif len(st1) == 0:
      st1.add(S[j])
  for j in idx2:
    if T[j] not in st2 and len(st2) > 0:
      print('No')
      exit()
    elif len(st2) == 0:
      st2.add(T[j])
      
print('Yes')