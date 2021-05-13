N=list(input())
s=set(N)
ans=''.join(sorted(s))
all=[chr(i) for i in range(97,97+26)]
if ans=='abcdefghijklmnopqrstuvwxyz':
  print('None')
  exit()
for i in range(len(ans)):
  if ans[i]!=all[i]:
    print(all[i])
    exit()
  elif i==len(ans)-1 :
    print(all[len(ans)])
    exit()