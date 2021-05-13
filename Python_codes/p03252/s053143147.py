S = list(input())
T = list(input())
N = len(S)

abc = 'abcdefghijklmnopqrstuvwxyz'
sviewed = {c:False for c in abc}
spair = {}

tviewed = {c:False for c in abc}
tpair = {}

for i in range(N):
  si = S[i]
  ti = T[i]
  if sviewed[si] == True:
    if spair[si] != ti:
      print('No')
      exit()
  else:
    sviewed[si] = True
    spair[si] = ti
    
  if tviewed[ti] == True:
    if tpair[ti] != si:
      print('No')
      exit()
  else:
    tviewed[ti] = True
    tpair[ti] = si
    
print('Yes')
