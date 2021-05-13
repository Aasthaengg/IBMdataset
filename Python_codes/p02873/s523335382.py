S = input()

bf = ''
idx = []
bdiff = 0
diff = 0
rlt = 0

for i in range(len(S)):
  if bf != S[i]:
    idx.append(i)
  bf = S[i]

idx.append(len(S))
for i in range(len(idx)-1): 
  diff = idx[i+1] - idx[i]
  rlt += diff*(diff+1)//2
  if S[idx[i]] == '>':
    if bdiff < diff:
      rlt -= bdiff
    else:
      rlt -= diff
  bdiff = diff

print(rlt)