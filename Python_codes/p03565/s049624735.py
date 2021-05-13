import sys
sp=input()
t=input()

m=len(sp)
n=len(t)
for i in range(m-n,-1,-1):
  cand=sp[:i].replace('?','a')+t+sp[i+n:].replace('?','a')
  for j,w in enumerate(t):
    if sp[j+i]!=w and sp[j+i]!='?':
      break
  else:
    print(cand)
    sys.exit()
print('UNRESTORABLE')