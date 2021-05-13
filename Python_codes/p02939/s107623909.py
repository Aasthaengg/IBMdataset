S=input()
ret = ['']
tmp = ''
for i in range(len(S)):
  tmp += S[i]
  if tmp == ret[-1]:
    continue
  else:
    ret.append(tmp)
    tmp=''
print(len(ret)-1)